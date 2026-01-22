# Mobile Development Rules

## Platform Guidelines

### iOS Development
- **Follow Apple HIG** (Human Interface Guidelines)
- **Use Swift** as primary language
- **Support latest iOS version** + 2 back
- **Test on physical devices** only
- **App Store compliance** required

### Android Development
- **Follow Material Design** guidelines
- **Use Kotlin** as primary language
- **Support latest Android** + 2 versions back
- **Test on multiple screen sizes**
- **Play Store compliance** required

## Cross-Platform Rules

### React Native
```typescript
// ✅ Good: Platform-specific components
import { Platform, StyleSheet } from 'react-native';

const styles = StyleSheet.create({
  container: {
    ...Platform.select({
      ios: {
        shadowColor: '#000',
        shadowOffset: { width: 0, height: 2 },
        shadowOpacity: 0.1,
        shadowRadius: 4,
      },
      android: {
        elevation: 4,
      },
    }),
  },
});

// ❌ Bad: No platform adaptation
const styles = StyleSheet.create({
  container: {
    elevation: 4, // Only works on Android
  },
});
```

### Flutter
```dart
// ✅ Good: Adaptive widgets
Widget build(BuildContext context) {
  return AdaptiveScaffold(
    // Automatically adapts to platform
    drawer: DrawerList(),
    body: ContentArea(),
  );
}
```

## Performance Rules

### Startup Time
| Metric | Target |
|--------|--------|
| Time to interactive (iOS) | < 2 seconds |
| Time to interactive (Android) | < 2 seconds |
| Cold start (iOS) | < 5 seconds |
| Cold start (Android) | < 5 seconds |

### Memory Limits
- **iOS App Store**: Max 4GB for download
- **Android Play Store**: Max 150MB for initial download
- **RAM usage**: Stay under 100MB typical
- **Image sizes**: Compress and lazy load

### Optimization Techniques
1. **Code splitting**: Load features on demand
2. **Image optimization**: WebP format, proper sizing
3. **Lazy loading**: Images, lists, routes
4. **Caching**: Local storage, memoization
5. **Bundle size**: Tree shaking, dead code elimination

## Security Rules

### Data Storage
```swift
// ✅ Good: Keychain for secrets
let query: [String: Any] = [
    kSecClass as String: kSecClassGenericPassword,
    kSecAttrAccount as String: "api_token",
    kSecValueData as String: tokenData,
    kSecAttrAccessible as String: kSecAttrAccessibleWhenUnlockedThisDeviceOnly
]

// ❌ Bad: UserDefaults for secrets
UserDefaults.standard.set(token, forKey: "api_token")
```

### Network Security
- **HTTPS only** for API calls
- **Certificate pinning** for sensitive apps
- **Secure storage** for tokens
- **Input validation** on all inputs

## Testing Requirements

### Test Coverage
| Test Type | Minimum Coverage |
|-----------|-----------------|
| Unit tests | 80% |
| Integration tests | 60% |
| E2E tests | Critical paths |

### Device Testing Matrix
```
iOS:
- iPhone 14/15 (latest)
- iPhone SE (budget)
- iPad (tablet)

Android:
- Pixel 7/8 (flagship)
- Samsung Galaxy (popular)
- Budget device (entry-level)
```

## Accessibility

### Requirements
- **VoiceOver/TalkBack** support
- **Color contrast** WCAG AA (4.5:1)
- **Touch targets** minimum 44x44 points/dp
- **Dynamic type** support for text

### Testing
```typescript
// Check accessibility labels
expect(screen.getByLabelText('Submit button')).toBeTruthy();

// Test with screen reader
const accessibilityTree = await getAccessibilityTree();
expect(accessibilityTree.label).toBe('Submit button, double tap to activate');
```

## Store Submission

### App Store Checklist
- [ ] Screenshots for all sizes
- [ ] App Store description
- [ ] Privacy policy URL
- [ ] Demo account (if needed)
- [ ] Privacy nutrition labels
- [ ] Background modes (if used)

### Play Store Checklist
- [ ] Feature graphic
- [ ] Screenshots for all densities
- [ ] Short description
- [ ] Full description
- [ ] Privacy policy
- [ ] Data safety form
