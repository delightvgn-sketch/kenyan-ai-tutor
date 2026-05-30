"use client";

import { useState } from "react";
import Link from "next/link";
import { usePathname } from "next/navigation";
import {
  BookOpen, MessageSquare, HelpCircle, BarChart2,
  Calendar, Upload, Menu, X, LogOut, Bell, User, ChevronRight,
} from "lucide-react";

const NAV = [
  { href:"/dashboard", label:"Dashboard", icon:BookOpen       },
  { href:"/chat",      label:"AI Tutor",  icon:MessageSquare  },
  { href:"/quiz",      label:"Quiz",      icon:HelpCircle     },
  { href:"/progress",  label:"Progress",  icon:BarChart2      },
  { href:"/schedule",  label:"Schedule",  icon:Calendar       },
  { href:"/upload",    label:"Upload",    icon:Upload         },
];

export default function DashboardLayout({ children }: { children: React.ReactNode }) {
  const [open, setOpen] = useState(false);
  const pathname        = usePathname();
  const currentLabel    = NAV.find((n) => n.href === pathname)?.label ?? "Dashboard";

  return (
    <div className="min-h-screen bg-gray-50 flex">
      {open && (
        <div className="fixed inset-0 bg-black/60 backdrop-blur-sm z-40 lg:hidden"
          onClick={() => setOpen(false)} />
      )}

      <aside className={`fixed top-0 left-0 h-full w-64 bg-forest-950 z-50 flex flex-col
        transform transition-transform duration-300
        ${open ? "translate-x-0" : "-translate-x-full"}
        lg:translate-x-0 lg:static lg:z-auto`}>

        <div className="flex items-center justify-between px-5 py-5 border-b border-forest-800">
          <Link href="/dashboard" className="flex items-center gap-2.5">
            <div className="w-8 h-8 bg-forest-600 rounded-lg flex items-center justify-center">
              <BookOpen className="w-4 h-4 text-white" />
            </div>
            <span className="font-display font-bold text-white text-lg">
              Soma<span className="text-gold-400">Smart</span>
            </span>
          </Link>
          <button onClick={() => setOpen(false)} className="lg:hidden text-forest-400 hover:text-white">
            <X className="w-5 h-5" />
          </button>
        </div>

        <div className="px-4 pt-5">
          <div className="bg-forest-900/60 rounded-xl p-4 border border-forest-800 flex items-center gap-3">
            <div className="w-10 h-10 bg-gradient-to-br from-gold-400 to-gold-600 rounded-full flex items-center justify-center text-forest-950 font-bold text-sm shadow-lg">
              S
            </div>
            <div className="flex-1 min-w-0">
              <p className="text-white font-semibold text-sm truncate">Student Name</p>
              <p className="text-forest-400 text-xs">Form 4 &#8226; 6 subjects</p>
            </div>
            <ChevronRight className="w-4 h-4 text-forest-500 flex-shrink-0" />
          </div>
        </div>

        <nav className="flex-1 px-4 pt-6">
          <p className="text-forest-500 text-xs font-semibold tracking-widest uppercase mb-3 px-2">Study Tools</p>
          <ul className="space-y-1">
            {NAV.map(({ href, label, icon: Icon }) => {
              const active = pathname === href;
              return (
                <li key={href}>
                  <Link href={href} onClick={() => setOpen(false)}
                    className={`flex items-center gap-3 px-3 py-2.5 rounded-xl text-sm font-medium transition-all
                      ${active ? "bg-forest-600 text-white shadow-lg shadow-forest-600/25" : "text-forest-300 hover:bg-forest-800 hover:text-white"}`}>
                    <Icon className="w-5 h-5 flex-shrink-0" />
                    {label}
                    {active && <div className="ml-auto w-1.5 h-1.5 bg-gold-400 rounded-full" />}
                  </Link>
                </li>
              );
            })}
          </ul>
        </nav>

        <div className="px-4 pb-6 pt-4 border-t border-forest-800">
          <button className="w-full flex items-center gap-3 px-3 py-2.5 rounded-xl text-sm font-medium text-red-400 hover:bg-red-500/10 hover:text-red-300 transition-all">
            <LogOut className="w-5 h-5" />Log Out
          </button>
        </div>
      </aside>

      <div className="flex-1 flex flex-col min-w-0">
        <header className="bg-white border-b border-gray-200 px-4 sm:px-6 py-4 flex items-center justify-between sticky top-0 z-30 shadow-sm">
          <div className="flex items-center gap-4">
            <button onClick={() => setOpen(true)} className="lg:hidden p-2 text-gray-500 hover:bg-gray-100 rounded-lg">
              <Menu className="w-5 h-5" />
            </button>
            <div>
              <h1 className="font-display font-bold text-gray-900 text-lg">{currentLabel}</h1>
              <p className="text-gray-400 text-xs">
                {new Date().toLocaleDateString("en-KE", { weekday:"long", day:"numeric", month:"long" })}
              </p>
            </div>
          </div>
          <div className="flex items-center gap-2">
            <button className="relative p-2 text-gray-500 hover:bg-gray-100 rounded-xl">
              <Bell className="w-5 h-5" />
              <span className="absolute top-1.5 right-1.5 w-2 h-2 bg-red-500 rounded-full" />
            </button>
            <button className="p-2 text-gray-500 hover:bg-gray-100 rounded-xl">
              <User className="w-5 h-5" />
            </button>
          </div>
        </header>
        <main className="flex-1 p-4 sm:p-6 overflow-auto">{children}</main>
      </div>
    </div>
  );
}
