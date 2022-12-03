import { login } from "@/api/user"
import { User } from "@/types/user"
import { removeToken } from "@/utils/api/auth/auth"
import { defineStore } from "pinia"
import { useRouter } from "vue-router"
export const useGlobalStore = defineStore("global", {
    state: () => {
        return {
            user: null as null | User,
        }
    },
    actions: {
        login(username: string, password: string) {
            login(username, password).then(({ data }) => {
                this.user = new User(data.user)
            })
        },
        logout() {
            this.user = null
            removeToken()
            useRouter().replace("/login")
        },
    },
})
