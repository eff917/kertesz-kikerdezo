/** @type {import('@sveltejs/kit').Config} */
import adapter from '@sveltejs/adapter-static';
const config = {
	kit: {
		// hydrate the <div id="svelte"> element in src/app.html
		target: '#svelte',
		adapter: adapter({
			pages: 'build',
			assets: 'build',
			fallback: null
		}),
		vite: {
			server: {
				proxy: {
					'/api': {
						target: 'http://127.0.0.1:8000',
						changeOrigin: true
					},
					'/static': {
						target: 'http://127.0.0.1:8000',
						changeOrigin: true
					}
				}
			}
		}
	}
};

export default config;
