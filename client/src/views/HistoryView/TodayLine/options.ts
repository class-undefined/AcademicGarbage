import { EChartsOption } from "echarts"
const colors = ["#3794FF"]
export const createLineOption = (
    labels: string[],
    data: number[]
): EChartsOption => {
    return {
        legend: {
            show: true,
            orient: "horizontal",
            data: ["今日识别统计"],
            right: 0,
        },
        tooltip: {
            show: true,
            trigger: "axis",
            textStyle: { color: "#424242" },
            axisPointer: {
                type: "cross",
            },
        },
        xAxis: {
            name: "今日时段使用频率",
            nameGap: 27,
            nameLocation: "middle",
            type: "category",
            data: labels,
            nameTextStyle: {
                padding: [0, 0, 0, 0],
            },
            axisLabel: {
                formatter: (value: string, index: number) => value,
            },
            axisLine: {
                symbol: ["none", "none"],
                symbolOffset: [0, 0],
                symbolSize: [10, 15],
            },
            splitLine: {
                show: false,
            }
        },
        yAxis: [
            {
                name: "次数",
                type: "value",
                axisLabel: {
                    formatter: `{value|{value}}`,
                    rich: {
                        base: {
                            fontSize: 12,
                        },
                        value: {
                            fontSize: 10,
                            padding: [0, 0, 0, 0],
                        },
                    },
                },
                nameTextStyle: {
                    padding: [0, 0, 0, 25],
                },
                axisLine: {
                    show: true,
                    symbol: ["none", "none"],
                    lineStyle: {
                        color: "#3794FF",
                    },
                },
                splitNumber: 1,
                splitLine: {
                    show: false,
                },
            },
        ],
        series: [
            {
                data,
                yAxisIndex: 0,
                type: "line",
                name: "识别次数",
                smooth: true,
                itemStyle: { color: colors[0] },
                lineStyle: { width: 3, color: colors[0] },
            },
        ],
    }
}
