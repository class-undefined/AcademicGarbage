import { io, Socket } from "socket.io-client"
import {requestConfig} from "@/request.config"
import { showSuccessToast, showFailToast, showLoadingToast } from 'vant'
import { getToken } from "@/utils/api/auth/auth"
import { EventsHandle } from "./types/task"



export class SocketIO {
    private socket: null | Socket

    constructor() {
        this.socket = null
    }

    /**
     * 建立socket通信
     * @returns 
     */
    public connect() {
        if (this.socket) return Promise.resolve(this)
        return new Promise<SocketIO>((resolve, reject) => {
            this.socket = io(requestConfig.ws)
            const loading = showLoadingToast({message: "建立会话中", duration: 0})
            this.socket.on("connected", () => {
                this.socket!.emit("bind", getToken())
            })
            this.socket.on("binded", () => {
                loading.close()
                showSuccessToast("会话已建立")
                resolve(this)
            })
            this.socket.on("connect_error", (e) => {
                reject(e)
            })
        })
    }

    /** 监听事件 */
    public on<Evt extends keyof EventsHandle>(event: Evt, callback: EventsHandle[Evt]) {
        // @ts-ignore
        this.socket.on(event, callback)
    }

}

const __gateway = new SocketIO()

/**获得包装后的Socket实例 */
export const getGateWay = () => __gateway.connect()