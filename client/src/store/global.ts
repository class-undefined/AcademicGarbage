import { User } from "@/types/user"
import { defineStore } from "pinia"
export const useGlobalStore = defineStore("global", {
    state: () => {
        return {
            user: null as null | User,
        }
    },
    actions: {
        login(username: string, password: string) {},
    },
})
