import { login, auth } from "@/api/user"
import { User } from "@/types/user"
import { removeToken, setToken } from "@/utils/api/auth/auth"
import { defineStore } from "pinia"
import { useRouter } from "vue-router"
export const useGlobalStore = defineStore("global", {
    state: () => {
        return {
            user: null as null | User,
            authLoading: false,
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
            this.authLoading = true
            return auth()
                .then(({ data }) => {
                    this.user = new User(data.user)
                })
                .finally(() => (this.authLoading = false))
        },
        logout() {
            this.user = null
            removeToken()
            useRouter().replace("/login")
        },
    },
})
