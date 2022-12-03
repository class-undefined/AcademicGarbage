import { defineConfig } from "vite"
import vue from "@vitejs/plugin-vue"
import Components from "unplugin-vue-components/vite"
import { VantResolver } from "unplugin-vue-components/resolvers"
import { resolve } from "path"
// https://vitejs.dev/config/
export default defineConfig({
	plugins: [
		vue(),
		Components({
			resolvers: [VantResolver()],
		}),
	],
	resolve: {
		alias: {
			"@": resolve("src"),
			"@assets": resolve("src/assets"),
			"@comps": resolve("src/components"),
			"@utils": resolve("src/utils"),
			"@router": resolve("src/router"),
			"@store": resolve("src/store"),
		},
	},
})
