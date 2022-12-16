import { service } from "@/utils/api/service/service"
import { Response } from "@/utils/api/response/type"
import { IUser } from "@/types/user"
import { IPhoto } from "@/types/photo"
type LoginResult = {
    token: string
    user: IUser
}

export const login = (username: string, password: string) => {
    return service({
        url: "/user/login",
        method: "POST",
        data: { username, password },
    }) as unknown as Promise<Response<LoginResult>>
}

export const register = (username: string, password: string) => {
    return service({
        url: "/user/register",
        method: "POST",
        data: { username, password },
    }) as unknown as Promise<Response<LoginResult>>
}

export const auth = () => {
    return service({
        url: "/user/login",
        method: "POST",
        data: { auth: true }
    }) as unknown as Promise<Response<LoginResult>>
}

export const addPhoto = () => {
    return service({
        url: "/user/add_photo",
        method: "POST",
        data: { auth: true }
    }) as unknown as Promise<Response<LoginResult>>
}

export const getPhotos = () => {
    return service({
        url: "/user/history",
        method: "GET",
        data: { auth: true }
    }) as unknown as Promise<Response<IPhoto[]>>
}