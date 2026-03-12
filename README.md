# 智慧便利店实时监控系统

基于 **Vue 3 + Three.js + Tailwind CSS + Flask** 的前后端分离实时监控大屏系统。

## 技术栈

### 前端
- **Vue 3** - 渐进式 JavaScript 框架
- **Vue Router** - 路由管理
- **Pinia** - 状态管理
- **Three.js** - 3D 可视化效果
- **ECharts** - 图表可视化
- **Tailwind CSS** - 原子化 CSS 框架
- **Socket.IO Client** - WebSocket 实时通信
- **Axios** - HTTP 请求库
- **Vite** - 构建工具

### 后端
- **Flask** - Python Web 框架
- **Flask-SocketIO** - WebSocket 支持
- **Flask-CORS** - 跨域支持
- **PyMySQL** - MySQL 数据库连接
- **Pandas** - 数据分析

## 项目结构

```
smart_store_monitor/
├── backend/                 # 后端 Flask API
│   ├── app.py              # 主应用入口
│   ├── config.py           # 数据库配置
│   ├── dao.py              # 数据访问层
│   ├── models.py           # 数据模型
│   ├── service.py          # 业务逻辑层
│   └── requirements.txt    # Python 依赖
│
├── frontend/               # 前端 Vue 项目
│   ├── src/
│   │   ├── api/           # API 接口封装
│   │   ├── assets/        # 静态资源
│   │   ├── router/        # 路由配置
│   │   ├── store/         # Pinia 状态管理
│   │   └── views/         # 页面组件
│   │       ├── Login.vue      # 登录页
│   │       ├── Dashboard.vue  # 监控大屏
│   │       └── Manage.vue     # 订单管理
│   ├── index.html
│   ├── package.json
│   ├── vite.config.js
│   ├── tailwind.config.js
│   └── postcss.config.js
│
├── start.bat              # Windows 启动脚本
├── start.sh               # Linux/Mac 启动脚本
└── README.md
```

## 功能特性

- **实时数据监控** - WebSocket 推送客流、营业额等数据
- **3D 可视化** - Three.js 实现粒子背景和店内热力图
- **数据图表** - ECharts 展示品类排行和客流波动
- **订单管理** - 增删改查、分页、筛选功能
- **响应式设计** - Tailwind CSS 实现现代化 UI
- **前后端分离** - RESTful API + 独立前端项目

## 快速开始

### 环境要求

- Python 3.8+
- Node.js 18+
- MySQL 5.7+

### 1. 配置数据库

修改 `backend/config.py` 中的数据库连接信息：

```python
DB_CONFIG = {
    'host': '127.0.0.1',
    'port': 3306,
    'user': 'root',
    'password': 'your_password',
    'database': 'smart_store',
    'charset': 'utf8mb4'
}
```

### 2. 安装后端依赖

```bash
cd backend
pip install -r requirements.txt
```

### 3. 安装前端依赖

```bash
cd frontend
npm install
```

### 4. 启动项目

**Windows:**
```bash
start.bat
```

**Linux/Mac:**
```bash
chmod +x start.sh
./start.sh
```

**或手动启动:**

```bash
# 后端
cd backend
python app.py

# 前端 (新终端)
cd frontend
npm run dev
```

### 5. 访问系统

- 前端地址: http://localhost:5173
- 后端 API: http://127.0.0.1:5000
- 默认账号: **admin / 123456**

## API 接口

| 接口 | 方法 | 说明 |
|------|------|------|
| `/api/auth/login` | POST | 用户登录 |
| `/api/auth/logout` | POST | 退出登录 |
| `/api/auth/check` | GET | 检查登录状态 |
| `/api/orders` | GET | 获取订单列表 |
| `/api/order/add` | POST | 新增订单 |
| `/api/order/update` | POST | 更新订单 |
| `/api/order/delete/<id>` | DELETE | 删除订单 |
| `/api/offline-stats` | GET | 品类销售排行 |
| `/api/realtime-state` | GET | 实时状态 |

## WebSocket 事件

- `store_update` - 实时推送店铺状态更新

## 截图预览

### 登录页面
- Three.js 粒子动画背景
- 玻璃拟态卡片设计

### 监控大屏
- 实时营业额、客流统计卡片
- 品类营业额排行柱状图
- 实时客流监控折线图
- 店内 3D 热力图可视化

### 订单管理
- 数据表格展示
- 多条件筛选
- 分页导航
- 新增/编辑/删除操作

## 开发说明

### 前端开发

```bash
cd frontend
npm run dev     # 开发模式
npm run build   # 生产构建
```

### 后端开发

```bash
cd backend
python app.py   # 启动开发服务器
```

## License

MIT
