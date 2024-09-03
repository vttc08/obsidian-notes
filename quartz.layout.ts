import { PageLayout, SharedLayout } from "./quartz/cfg"
import * as Component from "./quartz/components"
const mapTitle = "Digital Garden"

// components shared across all pages
export const sharedPageComponents: SharedLayout = {
  head: Component.Head(),
  header: [],
  afterBody: [],
  footer: Component.Footer({
    links: {
      GitHub: "https://github.com/jackyzha0/quartz",
      "Discord Community": "https://discord.gg/cRFFHYye7t",
    },
  }),
}

// components for pages that display a single page (e.g. a single note)
export const defaultContentPageLayout: PageLayout = {
  beforeBody: [
    Component.Breadcrumbs(),
    Component.ArticleTitle(),
    Component.ContentMeta(),
    Component.TagList(),
    Component.OnlyFor({titles: [mapTitle]}, Component.Explorer()),
    Component.OnlyFor({titles: [mapTitle]}, Component.RecentNotes({limit: 6})),
    Component.MobileOnly(Component.TableOfContents()),
    
  ],
  left: [
    Component.PageTitle(),
    Component.MobileOnly(Component.Spacer()),
    Component.Search(),
    Component.Darkmode(),
    Component.DesktopOnly(Component.Explorer()),
    Component.MobileOnly(Component.Map()),
  ],
  right: [
    Component.Backlinks(),
    Component.DesktopOnly(Component.TableOfContents()),
    Component.RecentNotes(),
    Component.Graph(),
  ],
}

// components for pages that display lists of pages  (e.g. tags or folders)
export const defaultListPageLayout: PageLayout = {
  beforeBody: [Component.Breadcrumbs(), Component.ArticleTitle(), Component.ContentMeta()],
  left: [
    Component.PageTitle(),
    Component.MobileOnly(Component.Spacer()),
    Component.Search(),
    Component.Darkmode(),
    Component.DesktopOnly(Component.Explorer()),
    Component.MobileOnly(Component.Map()),
  ],
  right: [],
}
