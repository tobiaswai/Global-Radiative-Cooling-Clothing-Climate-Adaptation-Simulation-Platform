"use client";

import Link from "next/link";
import { usePathname } from "next/navigation";
import { useState } from "react";

import { NAV_LINKS } from "@/config/navigation";

function isActivePath(pathname: string, href: string): boolean {
  return pathname === href || pathname.startsWith(`${href}/`);
}

export function NavBar() {
  const pathname = usePathname();
  const [isMobileMenuOpen, setIsMobileMenuOpen] = useState(false);

  return (
    <header className="border-b border-slate-800 bg-slate-950">
      <nav className="mx-auto flex min-h-16 w-full items-center justify-between px-4 sm:px-6 lg:px-8">
        <Link
          href="/simulations"
          className="font-semibold text-white"
          onClick={() => setIsMobileMenuOpen(false)}
        >
          Global Radiative Cooling Clothing Climate Adaptation Simulation Platform
        </Link>

        {/* Desktop navigation */}
        <div className="hidden items-center gap-6 md:flex">
          {NAV_LINKS.map((link) => {
            const active = isActivePath(pathname, link.href);

            return (
              <Link
                key={link.href}
                href={link.href}
                aria-current={active ? "page" : undefined}
                className={
                  active
                    ? "text-sm font-semibold text-blue-400"
                    : "text-sm font-medium text-slate-300 transition-colors hover:text-white"
                }
              >
                {link.label}
              </Link>
            );
          })}
        </div>

        {/* Mobile menu button */}
        <button
          type="button"
          className="rounded-md border border-slate-700 px-3 py-2 text-sm text-slate-200 hover:bg-slate-900 md:hidden"
          aria-label="Toggle navigation menu"
          aria-expanded={isMobileMenuOpen}
          onClick={() => {
            setIsMobileMenuOpen((current) => !current);
          }}
        >
          {isMobileMenuOpen ? "Close" : "Menu"}
        </button>
      </nav>

      {/* Mobile navigation */}
      {isMobileMenuOpen && (
        <div className="border-t border-slate-800 bg-slate-950 px-4 py-3 md:hidden">
          <div className="flex flex-col gap-1">
            {NAV_LINKS.map((link) => {
              const active = isActivePath(pathname, link.href);

              return (
                <Link
                  key={link.href}
                  href={link.href}
                  aria-current={active ? "page" : undefined}
                  onClick={() => setIsMobileMenuOpen(false)}
                  className={
                    active
                      ? "rounded-md bg-blue-950/50 px-3 py-2 text-sm font-semibold text-blue-400"
                      : "rounded-md px-3 py-2 text-sm font-medium text-slate-300 hover:bg-slate-900 hover:text-white"
                  }
                >
                  {link.label}
                </Link>
              );
            })}
          </div>
        </div>
      )}
    </header>
  );
}