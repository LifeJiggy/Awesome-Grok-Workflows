# Frontend Performance Rules

## Loading Performance
1. **Code Splitting** - Load only what's needed
2. **Lazy Loading** - Defer non-critical resources
3. **Tree Shaking** - Remove unused code
4. **Minification** - Reduce file sizes

## Rendering Performance
1. **Virtual Scrolling** - For long lists
2. **Memoization** - Avoid unnecessary re-renders
3. **Efficient Styling** - Avoid layout thrashing
4. **Web Workers** - Offload heavy computation

## Image Optimization
1. **Modern Formats** - WebP, AVIF
2. **Responsive Images** - Right size for device
3. **Lazy Loading** - Load on scroll
4. **Compression** - Optimize quality/size

## Network Performance
1. **HTTP/2** - Multiplexed requests
2. **Compression** - Gzip, Brotli
3. **Preloading** - Preload critical resources
4. **Service Workers** - Offline caching

## Core Web Vitals
1. **LCP** - Largest Contentful Paint < 2.5s
2. **FID** - First Input Delay < 100ms
3. **CLS** - Cumulative Layout Shift < 0.1
4. **Monitoring** - Track in production
