# Game Development Rules

## Architecture
1. **Entity-Component-System (ECS)** - For complex game entities
2. **Separation of concerns** - View, Logic, Data layers
3. **Event-driven communication** - Decouple systems
4. **Object pooling** - Avoid garbage collection spikes

## Performance
1. **60 FPS target** - 16.67ms frame budget
2. **Profiling first** - Measure before optimizing
3. **Level-of-detail (LOD)** - Scale complexity with distance
4. **Occlusion culling** - Don't render what player can't see

## Asset Management
1. **Compression formats** - Use appropriate codecs
2. **Streaming** - Load assets on-demand
3. **Asset bundles** - Group related assets
4. **Version control** - Large binary files with LFS

## Physics
1. **Determinism** - Same input = same output (for multiplayer)
2. **Collision layers** - Optimize collision detection
3. **Physics interpolation** - Smooth movement
4. **Rigid body hierarchy** - Minimize complex joints

## Multiplayer
1. **Client-side prediction** - Reduce perceived latency
2. **Server reconciliation** - Correct client state
3. **Lag compensation** - Handle latency gracefully
4. **Anti-cheat** - Validate server-side

## User Experience
1. **Input buffering** - Responsive controls
2. **Frame-rate independence** - Delta-time based movement
3. **Accessibility** - Colorblind modes, subtitles, remappable controls
4. **Loading screens** - Progress indicators, tips

## Grok Note
- "Optimization without profiling is like guessing in physics — you'll probably be wrong"
- Profile early, profile often
- Memory is often the bottleneck, not CPU
