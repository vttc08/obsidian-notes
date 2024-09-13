Wallabag, PHP, recent
Shirori, Go, 2 weeks ago
ArchiveBox
Readeck, Go, recent

Bookmarking
Permenantly saving archived for offline
Update page (if applicable)
Reddit support
Browser extension
WebUI with decent mobile app
subpath, authentication, PUGID

Shiori
- No reddit support except for text
- Some site not even images supported

Wallabag (require SSL, amd64 only)
- not support reddit (not formatted, no images/videos)
- imgur is supported
- support medium paywall/medium
Save images and data separately
Do not want to run as non-root. User makes container fail to run.  Even using chown, the container now encounters permission error.
Settings -> Misc -> Download images locally

Readeck
- not support reddit comments, YouTube, imgur
- only reddit post is archived
- Medium paywall support is spotty
- no option to refetch
- offline archiving stored in .zip file in data folder
require user 1000 1001 fix for permission
by default need login, but shared not need
Clean interface, fast. Very lightweight
Survived backup and restore by filesystem copy.
Multiuser support but no SSO

YouTube
Pinchflat
- idle usage up to 1%
- if something is deleted on the filesystem it will not be reflected in app
- nothing will be done for files deleted manually
- when setting date ranges, it automatically get pending but to download these it has to be manual
- to have a liked video instantly available a force index needs done
- source profile has to be set right the first time as changes won't be reflected later
- tries to index basically everything first time
TubeSync
- it attempts to save everything and index everything
Tube Archivist (python)
- requires redis and elasticsearch
- only works to skip sponsors in the web player but not locally

Custom Solution
- parse YouTube RSS feed
- manually parse videos and upload date
- every time the process finish write the date to a file and use it to compare