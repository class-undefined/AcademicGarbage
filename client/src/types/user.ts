import { getPhotos } from "@/api/user"
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

    /** 从服务器获取所有图片, 一并将user更新 */
    public async refreshPhotos() {
        return getPhotos().then(({ data }) => {
            this.photos = data.map(photo => new Photo(photo))
            return this.photos
        })
    }

    /** 平均识别率 */
    public totalAccuracy() {
        if (this.photos.length === 0) return 0
        let accuracy = 0
        for (const photo of this.photos) accuracy += photo.accuracy
        return accuracy / this.photos.length
    }

    /** 今日平均识别率 */
    public todayAccuracy() {
        const photos = this.getTodayPhotos()
        if (photos.length === 0) return 0
        let accuracy = 0
        for (const photo of photos) accuracy += photo.accuracy
        return accuracy / photos.length
    }

    /** 得到今天上传的图片 */
    public getTodayPhotos() {
        return this.photos.filter(photo => photo.isTodayCreated())
    }
}
