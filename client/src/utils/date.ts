// // 定义每周的日期范围

// import { Photo } from "@/types/photo"

// const getWeeklyDataCounts = (photos: Photo[]) => {
//     const weekRanges = [
//         [1, 7],
//         [8, 14],
//         [15, 21],
//         [22, 28],
//         [29, 31],
//     ]
//     // 初始化每周的数据总数为0
//     const weeklyDataCounts = {} as { [key: string]: number }
//     weekRanges.forEach(([start, end]) => {
//         weeklyDataCounts[`周 ${start}-${end}`] = 0
//     })

//     // 遍历每条数据，并统计每周的数据总数
//     photos.forEach(item => {
//         // 使用Date对象处理日期
//         const date = new Date(item.update_time)
//         // 获取这一天是这一年的第几天
//         const dayOfYear = date.getDate()
//         // 遍历每个日期范围，并根据日期判断数据属于哪一周
//         weekRanges.forEach(([start, end], index) => {
//             if (dayOfYear >= start && dayOfYear <= end) {
//                 // 将数据总数加1
//                 weeklyDataCounts[`第 ${start}-${end} 周`] += 1
//             }
//         })
//     })

//     return weeklyDataCounts
// }

// function drawChart(photos: Photo[]) {
//     // 获取每周的数据总数
//     const weeklyDataCounts = getWeeklyDataCounts(photos)

//     // 设置图表配置项
//     const options = {
//         xAxis: {
//             type: "category",
//             data: Object.keys(weeklyDataCounts),
//         },
//         yAxis: {
//             type: "value",
//         },
//         series: [
//             {
//                 data: Object.values(weeklyDataCounts),
//                 type: "line",
//             },
//         ],
//     }

//     // 初始化图表
//     const chart = echarts.init(document.getElementById("chart"))
//     // 使用配置项绘制图表
//     chart.setOption(options)
// }

export { }