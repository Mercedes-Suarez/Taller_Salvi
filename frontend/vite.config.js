import { defineConfig } from 'vite';
import react from '@vitejs/plugin-vue';

export default defineConfig({
  plugins: [react()],
  resolve: {
    alias: {
      '@': '/src',
      'jwt-decode': '/node_modules/jwt-decode/build/esm/index.js',
    }
  } 
  });