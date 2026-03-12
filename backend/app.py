import time
import random
import threading
from functools import wraps
from datetime import datetime
from flask import Flask, jsonify, request, session
from flask_socketio import SocketIO, emit
from flask_cors import CORS
from dao import init_db, insert_order, insert_visit, verify_user, get_filtered_orders, delete_order, update_order
from service import AnalyticsService, RealtimeService

app = Flask(__name__)
app.config['SECRET_KEY'] = 'smart_store_secure_key_2026'
CORS(app, supports_credentials=True, origins=["http://localhost:5173", "http://127.0.0.1:5173"])
socketio = SocketIO(app, cors_allowed_origins=["http://localhost:5173", "http://127.0.0.1:5173"])

def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'logged_in' not in session:
            return jsonify({"code": 401, "msg": "未登录，请先登录"}), 401
        return f(*args, **kwargs)
    return decorated_function

def background_sensor_simulator():
    categories = ['鲜食便当', '碳酸饮料', '休闲零食', '乳制品', '日用百货']
    while True:
        time.sleep(2.5)
        now = datetime.now()
        time_str = now.strftime("%H:%M:%S")
        
        change = random.choice([-1, 0, 1, 1])
        action = 'enter' if change > 0 else ('exit' if change < 0 else 'none')
        
        if action != 'none':
            insert_visit(action)
            if action == 'exit' and random.random() > 0.6:
                cat = random.choice(categories)
                amount = round(random.uniform(5.0, 50.0), 2)
                insert_order(cat, amount)
            RealtimeService.process_sensor_event(action)

        RealtimeService.sync_revenue_from_db()
        state = RealtimeService.get_current_state()
        RealtimeService.append_to_queue(time_str, state['current_inside'])
        
        socketio.emit('store_update', {
            'time': time_str,
            'current_inside': state['current_inside'],
            'revenue': state['revenue'],
            'visitors': state['visitors']
        })

@app.route('/api/auth/login', methods=['POST'])
def login():
    data = request.get_json() or {}
    username = data.get('username', '')
    password = data.get('password', '')
    
    if verify_user(username, password):
        session['logged_in'] = True
        session['username'] = username
        return jsonify({"code": 200, "msg": "登录成功", "data": {"username": username}})
    else:
        return jsonify({"code": 401, "msg": "用户名或密码错误"}), 401

@app.route('/api/auth/logout', methods=['POST'])
def logout():
    session.clear()
    return jsonify({"code": 200, "msg": "已退出登录"})

@app.route('/api/auth/check', methods=['GET'])
def check_auth():
    if 'logged_in' in session:
        return jsonify({"code": 200, "data": {"logged_in": True, "username": session.get('username')}})
    return jsonify({"code": 200, "data": {"logged_in": False}})

@app.route('/api/orders', methods=['GET'])
@login_required
def api_get_orders():
    category = request.args.get('category', '').strip()
    try:
        min_amount = float(request.args.get('min_amount')) if request.args.get('min_amount') else None
    except:
        min_amount = None
    try:
        max_amount = float(request.args.get('max_amount')) if request.args.get('max_amount') else None
    except:
        max_amount = None
    
    page = request.args.get('page', 1, type=int)
    per_page = 10

    orders, total_records = get_filtered_orders(
        category=category if category else None,
        min_amount=min_amount,
        max_amount=max_amount,
        page=page,
        per_page=per_page
    )
    
    return jsonify({
        "code": 200,
        "data": {
            "orders": orders,
            "total_records": total_records,
            "total_pages": (total_records + 9) // 10,
            "current_page": page
        }
    })

@app.route('/api/order/add', methods=['POST'])
@login_required
def api_add_order():
    data = request.get_json() or {}
    category = data.get('category', '')
    amount = float(data.get('amount', 0))
    insert_order(category, amount)
    RealtimeService.sync_revenue_from_db()
    return jsonify({"code": 200, "msg": "新增成功"})

@app.route('/api/order/update', methods=['POST'])
@login_required
def api_update_order():
    data = request.get_json() or {}
    order_id = int(data.get('id', 0))
    category = data.get('category', '')
    amount = float(data.get('amount', 0))
    update_order(order_id, category, amount)
    RealtimeService.sync_revenue_from_db()
    return jsonify({"code": 200, "msg": "修改成功"})

@app.route('/api/order/delete/<int:order_id>', methods=['DELETE'])
@login_required
def api_delete_order(order_id):
    delete_order(order_id)
    RealtimeService.sync_revenue_from_db()
    return jsonify({"code": 200, "msg": "删除成功"})

@app.route('/api/offline-stats', methods=['GET'])
@login_required
def api_offline_stats():
    data = AnalyticsService.get_category_sales_ranking()
    return jsonify({"code": 200, "data": data})

@app.route('/api/realtime-state', methods=['GET'])
@login_required
def api_realtime_state():
    state = RealtimeService.get_current_state()
    return jsonify({"code": 200, "data": state})

@socketio.on('connect')
def handle_connect():
    print('客户端已连接')
    state = RealtimeService.get_current_state()
    emit('store_update', {
        'time': datetime.now().strftime("%H:%M:%S"),
        'current_inside': state['current_inside'],
        'revenue': state['revenue'],
        'visitors': state['visitors']
    })

if __name__ == '__main__':
    init_db()
    RealtimeService.sync_revenue_from_db()
    threading.Thread(target=background_sensor_simulator, daemon=True).start()
    socketio.run(app, debug=True, port=5001, allow_unsafe_werkzeug=True)
