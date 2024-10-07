HTML attribute can be applied to a tag or element. Some attribute only work on certain elements (eg. datetime only work on time)
- **Global** works on any element
```html
<time attribute=123></time>
```

**Date Time** ^270b7d
Attribute that give a machine readable time format.
- `yyyy-mm-dd`, `hh:mm:ss`
- `hh-mm-ss(+/-)hh:mm` eg `12:30+3:00` means 12:30 in +3 timezone

**Class**
Global attribute that makes it easier for CSS and JS to select
*Lang/Dir* specify which language and which direction to read

**ID**
Similar to class, but unique. Only can be used once.

**Content Editable**
```html
<p contenteditable="true">Anyone can edit this.</p>
```

**Aria**
Aria makes it easier for accessibility readers.
```html
<p aria-label="Aria Text">Aria Text</p>
<p aria-hidden="true">Do not show to accessibility</p>
```
Use `aria-label` to show accessibility readers, use `aria-hidden` to hide the part to accessibility readers.

**href**
Hypertext references. Link to another page, image. ^36e9fb