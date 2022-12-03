import { createApp } from "vue"
import { createPinia } from "pinia"
import { router } from "./router"
import App from "./App.vue"
import "./style.scss"
import "vant/es/toast/style"
import "vant/es/dialog/style"
import "vant/es/notify/style"
import "vant/es/image-preview/style"
import ElementPlus from "element-plus"
import "element-plus/dist/index.css"
import "element-plus/theme-chalk/dark/css-vars.css"
import { useDark, useToggle } from "@vueuse/core"
const isToggle = useToggle(useDark())
isToggle(true)
createApp(App).use(ElementPlus).use(createPinia()).use(router).mount("#app")
