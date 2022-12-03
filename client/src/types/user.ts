import { Photo, IPhoto } from "./photo"

export interface IUser {
    username: string
    photos: IPhoto[]
}
export class User implements IUser {
    public username: string
    public photos: Photo[]
    constructor(user: IUser) {
        this.username = user.username
        this.photos = user.photos.map(photo => new Photo(photo))
    }
}
