import { Photo } from "@/types/photo"
import { Response } from "@/utils/api/response/type"
export type IdentifyResult = Response<{
    data: Photo,
    photo_id: string,
}>


export type EventsHandle = {
    accept_identify_rst: (result: IdentifyResult) => void
}