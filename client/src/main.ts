import { createApp } from "vue"
import { createPinia } from "pinia"
import router from "./router"
import App from "./App.vue"
import "./style.css"
import "vant/es/toast/style"
import "vant/es/dialog/style"
import "vant/es/notify/style"
import "vant/es/image-preview/style"

createApp(App).use(createPinia()).use(router).mount("#app")
