import { login, auth, register, getPhotos } from "@/api/user"
import { User } from "@/types/user"
import { removeToken, setToken } from "@/utils/api/auth/auth"
import { defineStore } from "pinia"
import { useRouter } from "vue-router"
import { showFailToast, showLoadingToast } from "vant"
import { Photo } from "@/types/photo"
export const useGlobalStore = defineStore("global", {
    state: () => {
        return {
            user: null as null | User
        }
    },
    actions: {
        async login(username: string, password: string) {
            return login(username, password).then(({ data }) => {
                this.user = new User(data.user)
                setToken(data.token)
            })
        },
        async register(username: string, password: string) {
            if (username.trim().length === 0 || password.trim().length === 0) {
                showFailToast({
                    message: "账号或密码不可为空",
                    duration: 3000
                })
            }
            return register(username, password).then(({ data }) => {
                this.user = new User(data.user)
                setToken(data.token)
            })

        },
        /** token验证 */
        async auth() {
            const toast = showLoadingToast({
                message: "获取登录信息",
                forbidClick: true,
            })
            return auth()
                .then(({ data }) => {
                    this.user = new User(data.user)
                })
                .finally(() => toast.close())
        },
        logout() {
            this.user = null
            removeToken()
            useRouter().replace("/login")
        },
        async refreshPhotos() {
            if (!this.user) throw "user不存在"
            return this.user.refreshPhotos()
        }
    },
})
