export interface IPhoto {
    id: string
    userid: string
    original_url: string
    processed_url: string
    create_time: Date
    update_time: Date
    accuracy: number
    helmets_count: number
}

export class Photo implements IPhoto {
    /** 图片id */
    public id: string

    /** 用户id */
    public userid: string

    /** 原始图片 */
    public original_url: string

    /** 处理后图片 */
    public processed_url: string

    /** 创建时间 */
    public create_time: Date

    /** 修改时间 */
    public update_time: Date

    /** 准确率 */
    public accuracy: number

    /** 安全帽 */
    public helmets_count: number
    constructor(photo: IPhoto) {
        this.id = photo.id
        this.userid = photo.userid
        this.original_url = photo.original_url
        this.processed_url = photo.processed_url
        this.create_time = new Date(photo.create_time)
        this.update_time = new Date(photo.update_time)
        this.accuracy = photo.accuracy
        this.helmets_count = photo.helmets_count
    }

    /** 是否为今天创建的图片 */
    public isTodayCreated() {
        const today = new Date();
        return (
            this.create_time.getFullYear() === today.getFullYear() &&
            this.create_time.getMonth() === today.getMonth() &&
            this.create_time.getDate() === today.getDate()
        )
    }
}
