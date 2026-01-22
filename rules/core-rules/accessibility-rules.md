# Accessibility Rules

## WCAG Compliance

### Conformance Levels
| Level | Description | Requirement |
|-------|-------------|-------------|
| A | Minimum | Must have |
| AA | Standard | Should have |
| AAA | Highest | Nice to have |

### Quick Reference
| Criterion | Level | Description |
|-----------|-------|-------------|
| 1.1.1 | A | Non-text content has alt text |
| 1.2.1 | A | Audio/video has alternatives |
| 1.3.1 | A | Content order is meaningful |
| 1.4.1 | A | Color not only convey meaning |
| 2.1.1 | A | Keyboard accessible |
| 2.4.1 | Bypass blocks |
| 2.4.4 | AA | Links have purpose |
| 2.4.7 | AA | Focus visible |
| 3.1.1 | A | Page language identified |
| 4.1.1 | A | No parsing errors |

## Visual Accessibility

### Color Contrast
```yaml
contrast_requirements:
  normal_text:
    aa: 4.5:1
    aaa: 7.0:1
    
  large_text:
    aa: 3.0:1
    aaa: 4.5:1
    
  ui_components:
    aa: 3.0:1
```

### Color Blindness Safe
```css
/* ❌ Bad: Red/Green only */
.status-success { color: red; }
.status-error { color: red; }

/* ✅ Good: Shape + Color */
.status-success { 
  color: #2e7d32;  /* Green */
  icon: check-circle;
}
.status-error { 
  color: #c62828;  /* Red */
  icon: alert-circle;
}
```

## Screen Reader Support

### Semantic HTML
```html
<!-- ✅ Good: Semantic structure -->
<header>
  <nav aria-label="Main navigation">
    <ul>
      <li><a href="/" aria-current="page">Home</a></li>
      <li><a href="/products">Products</a></li>
    </ul>
  </nav>
</header>

<main>
  <article>
    <h1>Page Title</h1>
    <p>Content...</p>
  </article>
</main>

<footer>...</footer>

<!-- ❌ Bad: Non-semantic -->
<div class="header">
  <div class="nav">
    <div>Home</div>
    <div>Products</div>
  </div>
</div>
```

### ARIA Attributes
```html
<!-- Interactive components -->
<button 
  aria-expanded="false"
  aria-controls="menu"
  aria-label="Open menu"
>
  Menu
</button>

<!-- Live regions -->
<div role="status" aria-live="polite">
  {{message}}
</div>

<!-- Form labels -->
<label for="email">Email address</label>
<input 
  id="email" 
  type="email" 
  aria-describedby="email-help"
>
<span id="email-help">
  We'll never share your email.
</span>
```

## Keyboard Navigation

### Focus Management
```typescript
// Trap focus in modal
function trapFocus(modal: HTMLElement) {
  const focusableElements = modal.querySelectorAll(
    'button, [href], input, select, textarea, [tabindex]:not([tabindex="-1"])'
  );
  
  const firstFocusable = focusableElements[0];
  const lastFocusable = focusableElements[focusableElements.length - 1];
  
  modal.addEventListener('keydown', (e) => {
    if (e.key === 'Tab') {
      if (e.shiftKey && document.activeElement === firstFocusable) {
        e.preventDefault();
        lastFocusable.focus();
      } else if (!e.shiftKey && document.activeElement === lastFocusable) {
        e.preventDefault();
        firstFocusable.focus();
      }
    }
  });
}
```

### Skip Links
```html
<!-- Skip to main content -->
<a href="#main-content" class="skip-link">
  Skip to main content
</a>

<style>
.skip-link {
  position: absolute;
  top: -40px;
  left: 0;
  background: #000;
  color: #fff;
  padding: 8px;
  z-index: 100;
}

.skip-link:focus {
  top: 0;
}
</style>

<main id="main-content">
  <!-- Page content -->
</main>
```

## Mobile Accessibility

### Touch Targets
```css
/* Minimum 44x44 CSS pixels */
.touch-target {
  min-width: 44px;
  min-height: 44px;
  display: flex;
  align-items: center;
  justify-content: center;
}

/* Spacing between targets */
.touch-target + .touch-target {
  margin-top: 8px;
}
```

### Responsive Text
```css
/* Respect user preferences */
html {
  font-size: 100%; /* Respect browser setting */
}

/* Support zoom */
@media (max-width: 320px) {
  body {
    font-size: 16px; /* Minimum for zoom */
  }
}
```

## Testing Checklist

### Automated Testing
- [ ] Run axe-core in CI
- [ ] Check color contrast
- [ ] Validate ARIA usage
- [ ] Test keyboard navigation
- [ ] Check heading structure

### Manual Testing
- [ ] Test with screen reader (NVDA, VoiceOver)
- [ ] Navigate by keyboard only
- [ ] Zoom to 200%
- [ ] Disable images
- [ ] Use high contrast mode

### Assistive Technology
| OS | Screen Reader | Browser |
|----|---------------|---------|
| Windows | NVDA, JAWS | Chrome, Firefox |
| macOS | VoiceOver | Safari, Chrome |
| iOS | VoiceOver | Safari |
| Android | TalkBack | Chrome |

## Documentation Requirements

### Accessibility Statement
```yaml
accessibility_statement:
  date: "2024-01-01"
  standard: "WCAG 2.1 Level AA"
  conformance: "Partially conformant"
  known_issues:
    - "Some older PDF documents not accessible"
    - "Video captions in progress"
  feedback: "accessibility@example.com"
```

### Alternative Formats
- Provide text alternatives
- Offer audio descriptions
- Create plain language versions
- Consider translations
