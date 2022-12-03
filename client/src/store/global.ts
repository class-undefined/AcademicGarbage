import { login, auth } from "@/api/user"
import { User } from "@/types/user"
import { removeToken, setToken } from "@/utils/api/auth/auth"
import { defineStore } from "pinia"
import { useRouter } from "vue-router"
import { showLoadingToast } from "vant"
export const useGlobalStore = defineStore("global", {
    state: () => {
        return {
            user: null as null | User,
        }
    },
    actions: {
        async login(username: string, password: string) {
            return login(username, password).then(({ data }) => {
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
    },
})
