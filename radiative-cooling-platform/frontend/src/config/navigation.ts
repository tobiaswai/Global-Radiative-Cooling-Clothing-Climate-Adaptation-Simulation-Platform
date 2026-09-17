export type NavLink = {
  href: string;
  label: string;
};

export const NAV_LINKS: NavLink[] = [
  {
    href: "/simulations",
    label: "Simulations",
  },
  {
    href: "/materials",
    label: "Materials",
  },
  {
    href: "/global-analysis",
    label: "Global Analysis",
  },
];
