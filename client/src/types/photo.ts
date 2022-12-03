export interface IPhoto {
    userid: string
    original_url: string
    processed_url: string
    create_time: Date
    update_time: Date
    accuracy: string
    helmets_count: string
}

export class Photo implements IPhoto {
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
    public accuracy: string

    /** 安全帽 */
    public helmets_count: string
    constructor(photo: IPhoto) {
        this.userid = photo.userid
        this.original_url = photo.original_url
        this.processed_url = photo.processed_url
        this.create_time = photo.create_time
        this.update_time = photo.update_time
        this.accuracy = photo.accuracy
        this.helmets_count = photo.helmets_count
    }
}
