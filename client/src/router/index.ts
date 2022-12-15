import { createRouter, createWebHistory, RouteRecordRaw } from "vue-router"
import HomeView from "@/views/HomeView.vue"
import RegisterView from "@/views/RegisterView.vue"
import LoginView from "@/views/LoginView.vue"
import HistoryView from "@/views/HistoryView/index.vue"
import { useGlobalStore } from "@/store/global"
const routes: Array<RouteRecordRaw> = [
    {
        path: "/",
        name: "home",
        component: HomeView,
        meta: {
            navbar: true, // 是否显示导航栏
            title: "主页",
            icon: "home-o", // 图标
            auth: true, // 需要验证
        },
    },
    {
        path: "/history",
        name: "history",
        component: HistoryView,
        meta: {
            navbar: true, // 是否显示导航栏
            title: "历史记录",
            icon: "clock-o", // 图标
            auth: true, // 需要验证
        },
    },
    {
        path: "/login",
        name: "login",
        component: LoginView,
        meta: {
            navbar: false,
            title: "登录",
            auth: false,
        },
    },
    {
        path: "/register",
        name: "register",
        component: RegisterView,
        meta: {
            navbar: false,
            title: "注册",
            auth: false,
        },
    },
]

const router = createRouter({
    history: createWebHistory("/"),
    routes,
})

router.beforeEach((to, from, next) => {
    // 如果需要验证, 则进行验证
    if (to.meta.auth) {
        const gloabl = useGlobalStore()
        if (!gloabl.user) {
            gloabl
                .auth()
                .then(() => next())
                .catch(() => {
                    router.push("/login")
                })
            return
        }
        next()
    } else {
        next()
    }
})

export { router, routes }
