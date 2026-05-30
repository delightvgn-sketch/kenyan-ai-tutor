#!/usr/bin/env python3
"""
SomaSmart Phase 2 — Frontend File Generator
Run from inside the frontend/ directory:
    python setup_files.py
"""
import os, sys

def write(path: str, content: str) -> None:
    d = os.path.dirname(path)
    if d:
        os.makedirs(d, exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(content)
    print(f"  created -> {path}")

if not os.path.exists("package.json"):
    print("\n ERROR: package.json not found.")
    print("   Run this from inside the frontend/ directory")
    print("   after running: pnpm create next-app@latest .\n")
    sys.exit(1)

print("\n SomaSmart - Phase 2 File Setup")
print("=" * 40)

# ── 1. tailwind.config.ts ─────────────────────────────────────────────────────
write("tailwind.config.ts", '''import type { Config } from "tailwindcss";

const config: Config = {
  content: [
    "./pages/**/*.{js,ts,jsx,tsx,mdx}",
    "./components/**/*.{js,ts,jsx,tsx,mdx}",
    "./app/**/*.{js,ts,jsx,tsx,mdx}",
  ],
  theme: {
    extend: {
      colors: {
        forest: {
          50:"#f0fdf4",100:"#dcfce7",200:"#bbf7d0",300:"#86efac",
          400:"#4ade80",500:"#22c55e",600:"#16a34a",700:"#15803d",
          800:"#166534",900:"#14532d",950:"#052e16",
        },
        gold:{300:"#fcd34d",400:"#fbbf24",500:"#f59e0b",600:"#d97706"},
      },
      fontFamily:{
        sans:["var(--font-nunito)","sans-serif"],
        display:["var(--font-raleway)","sans-serif"],
      },
      animation:{
        "fade-in":"fadeIn 0.5s ease-in-out",
        "slide-up":"slideUp 0.4s ease-out",
      },
      keyframes:{
        fadeIn:{"0%":{opacity:"0"},"100%":{opacity:"1"}},
        slideUp:{
          "0%":{opacity:"0",transform:"translateY(16px)"},
          "100%":{opacity:"1",transform:"translateY(0)"},
        },
      },
    },
  },
  plugins:[],
};
export default config;
''')

# ── 2. app/globals.css ────────────────────────────────────────────────────────
write("app/globals.css", '''@tailwind base;
@tailwind components;
@tailwind utilities;

@layer base {
  html { scroll-behavior: smooth; }
  body { @apply bg-gray-50 text-gray-900 font-sans; -webkit-font-smoothing: antialiased; }
  h1,h2,h3,h4,h5,h6 { @apply font-display; }
}

@layer components {
  .btn-primary {
    @apply inline-flex items-center justify-center gap-2 bg-forest-600 hover:bg-forest-700
           text-white font-semibold px-6 py-3 rounded-xl transition-all duration-200
           focus:outline-none focus:ring-2 focus:ring-forest-500 focus:ring-offset-2
           disabled:opacity-50 disabled:cursor-not-allowed;
  }
  .btn-secondary {
    @apply inline-flex items-center justify-center gap-2 bg-white hover:bg-gray-50
           text-forest-700 font-semibold px-6 py-3 rounded-xl border-2 border-forest-600
           transition-all duration-200;
  }
  .btn-ghost {
    @apply inline-flex items-center justify-center gap-2 text-gray-600 hover:text-gray-900
           hover:bg-gray-100 font-medium px-4 py-2 rounded-lg transition-all duration-200;
  }
  .card       { @apply bg-white rounded-2xl border border-gray-100 shadow-sm; }
  .card-hover { @apply card hover:shadow-md hover:border-gray-200 transition-all duration-200 cursor-pointer; }
  .input-field {
    @apply w-full px-4 py-3 rounded-xl border border-gray-300 focus:outline-none
           focus:ring-2 focus:ring-forest-500 focus:border-transparent bg-white
           text-gray-900 placeholder-gray-400 transition-all duration-200;
  }
  .badge       { @apply inline-flex items-center gap-1 px-2.5 py-1 rounded-full text-xs font-semibold; }
  .badge-green { @apply badge bg-forest-100 text-forest-700; }
  .badge-gold  { @apply badge bg-amber-100 text-amber-700; }
  .badge-red   { @apply badge bg-red-100 text-red-700; }
}

@layer utilities {
  .text-gradient {
    @apply bg-gradient-to-r from-forest-600 to-forest-400 bg-clip-text text-transparent;
  }
  .bg-kenya-pattern {
    background-image: radial-gradient(circle at 1px 1px, rgba(255,255,255,0.06) 1px, transparent 0);
    background-size: 28px 28px;
  }
}

::-webkit-scrollbar       { width: 5px; }
::-webkit-scrollbar-track { background: #f1f5f9; }
::-webkit-scrollbar-thumb { background: #cbd5e1; border-radius: 3px; }
::-webkit-scrollbar-thumb:hover { background: #94a3b8; }
''')

# ── 3. app/layout.tsx ─────────────────────────────────────────────────────────
write("app/layout.tsx", '''import type { Metadata } from "next";
import { Raleway, Nunito } from "next/font/google";
import "./globals.css";

const raleway = Raleway({
  subsets: ["latin"], variable: "--font-raleway", display: "swap",
  weight: ["400","500","600","700","800","900"],
});
const nunito = Nunito({
  subsets: ["latin"], variable: "--font-nunito", display: "swap",
  weight: ["400","500","600","700","800"],
});

export const metadata: Metadata = {
  title: "SomaSmart — AI Study Assistant for Kenyan Students",
  description: "AI-powered KCSE, 8-4-4 and CBC tutor. Step-by-step KNEC explanations, past paper analysis, quizzes, and personalised revision plans.",
  keywords: ["KCSE","Kenya","study","AI tutor","CBC","8-4-4","education"],
};

export default function RootLayout({ children }: { children: React.ReactNode }) {
  return (
    <html lang="en" className={`${raleway.variable} ${nunito.variable}`}>
      <body className="font-sans antialiased">{children}</body>
    </html>
  );
}
''')

# ── 4. app/page.tsx  (Landing Page) ───────────────────────────────────────────
write("app/page.tsx", '''import Link from "next/link";
import {
  BookOpen, Brain, Mic, FileText, BarChart2, Clock,
  ChevronRight, Sparkles, Shield, Globe, CheckCircle2,
} from "lucide-react";

const FEATURES = [
  { icon:Brain,     title:"AI Tutoring in KNEC Style", color:"text-forest-600", bg:"bg-forest-50",   desc:"Explains every concept step-by-step, exactly how KNEC examiners award marks." },
  { icon:FileText,  title:"Past Paper Analysis",        color:"text-blue-600",   bg:"bg-blue-50",    desc:"Upload KCSE past papers or photos of questions. The AI explains every mark scheme answer." },
  { icon:Mic,       title:"Voice Interaction",          color:"text-purple-600", bg:"bg-purple-50",  desc:"Ask questions by voice and hear explanations read back. Study hands-free, anytime." },
  { icon:BarChart2, title:"Weak Topic Detection",       color:"text-amber-600",  bg:"bg-amber-50",   desc:"The AI tracks where you struggle and builds a plan to close gaps before the exam." },
  { icon:Sparkles,  title:"Smart Quiz Generation",      color:"text-red-500",    bg:"bg-red-50",     desc:"Auto-generates KCSE-style quizzes on the exact topics you are revising." },
  { icon:Clock,     title:"Revision Scheduling",        color:"text-teal-600",   bg:"bg-teal-50",    desc:"Builds a timetable around your exam date, prioritising your weakest subjects first." },
];

const SUBJECTS = [
  "📐 Mathematics","🧪 Chemistry","🌿 Biology","📖 English",
  "🗣️ Kiswahili","🌍 Geography","📜 History","✝️ CRE",
  "🏠 Home Science","💻 Computer Studies","⚡ Physics","🌾 Agriculture",
];

const STEPS = [
  { num:"01", title:"Create Your Free Account",    desc:"Sign up in 60 seconds. Tell us your grade and subjects." },
  { num:"02", title:"Ask Any Question",            desc:"Type, speak, or upload a photo of your question." },
  { num:"03", title:"Get KCSE-Style Explanations", desc:"Receive step-by-step answers with mark scheme guidance." },
];

export default function LandingPage() {
  return (
    <div className="min-h-screen bg-white overflow-x-hidden">

      {/* Navbar */}
      <nav className="sticky top-0 z-50 bg-white/90 backdrop-blur-md border-b border-gray-100">
        <div className="max-w-6xl mx-auto px-4 sm:px-6 py-4 flex items-center justify-between">
          <div className="flex items-center gap-2.5">
            <div className="w-9 h-9 bg-forest-600 rounded-xl flex items-center justify-center shadow-sm">
              <BookOpen className="w-5 h-5 text-white" />
            </div>
            <span className="text-xl font-display font-bold text-gray-900">
              Soma<span className="text-forest-600">Smart</span>
            </span>
          </div>
          <div className="flex items-center gap-3">
            <Link href="/login"    className="btn-ghost text-sm">Log in</Link>
            <Link href="/register" className="btn-primary text-sm py-2">Get Started Free</Link>
          </div>
        </div>
      </nav>

      {/* Hero */}
      <section className="relative pt-20 pb-28 px-4 bg-gradient-to-b from-forest-950 via-forest-900 to-forest-800 bg-kenya-pattern overflow-hidden">
        <div className="absolute inset-0 overflow-hidden pointer-events-none">
          <div className="absolute -top-20 -right-20 w-96 h-96 bg-forest-600/20 rounded-full blur-3xl" />
          <div className="absolute -bottom-10 -left-10 w-64 h-64 bg-gold-500/10 rounded-full blur-2xl" />
        </div>
        <div className="relative max-w-4xl mx-auto text-center">
          <div className="inline-flex items-center gap-2 bg-forest-800/60 border border-forest-600/40 text-forest-300 px-4 py-2 rounded-full text-sm font-medium mb-8 backdrop-blur-sm">
            <Shield className="w-4 h-4" />
            Designed for KCSE, 8-4-4 &amp; CBC Students in Kenya
          </div>
          <h1 className="text-5xl sm:text-6xl lg:text-7xl font-display font-black text-white leading-tight mb-6">
            Your Personal{" "}
            <span className="bg-gradient-to-r from-gold-400 to-gold-300 bg-clip-text text-transparent">
              AI Teacher
            </span>
            {" "}&#8212; 24/7
          </h1>
          <p className="text-xl text-forest-200 max-w-2xl mx-auto mb-10 leading-relaxed">
            SomaSmart teaches like a real Kenyan teacher &#8212; step-by-step KNEC answers,
            past paper analysis, voice interaction, and personalised revision schedules.
          </p>
          <div className="flex flex-col sm:flex-row gap-4 justify-center">
            <Link href="/register" className="inline-flex items-center justify-center gap-2 bg-gold-500 hover:bg-gold-600 text-forest-950 font-bold text-lg px-8 py-4 rounded-xl transition-all hover:shadow-xl">
              Start Learning Free <ChevronRight className="w-5 h-5" />
            </Link>
            <Link href="/login" className="inline-flex items-center justify-center gap-2 bg-white/10 hover:bg-white/20 text-white font-bold text-lg px-8 py-4 rounded-xl border border-white/20 transition-all">
              I Have an Account
            </Link>
          </div>
          <p className="text-forest-400 text-sm mt-8 flex items-center gap-6 justify-center flex-wrap">
            {["100% Free","No credit card","Works on mobile"].map((t) => (
              <span key={t} className="flex items-center gap-1.5">
                <CheckCircle2 className="w-4 h-4" />{t}
              </span>
            ))}
          </p>
        </div>
      </section>

      {/* Subjects strip */}
      <section className="bg-forest-600 py-3">
        <div className="flex gap-8 flex-wrap justify-center px-4">
          {SUBJECTS.map((s) => (
            <span key={s} className="text-white/90 text-sm font-medium whitespace-nowrap">{s}</span>
          ))}
        </div>
      </section>

      {/* Features */}
      <section className="py-24 px-4 bg-gray-50">
        <div className="max-w-6xl mx-auto">
          <div className="text-center mb-16">
            <p className="text-forest-600 font-semibold text-sm tracking-widest uppercase mb-3">Why SomaSmart?</p>
            <h2 className="text-4xl sm:text-5xl font-display font-black text-gray-900 mb-5">
              Everything You Need to Excel in KCSE
            </h2>
            <p className="text-gray-500 text-xl max-w-2xl mx-auto">
              Not just a chatbot &#8212; a complete AI study system built for Kenyan students.
            </p>
          </div>
          <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
            {FEATURES.map((f) => {
              const Icon = f.icon;
              return (
                <div key={f.title} className="card-hover p-7">
                  <div className={`w-12 h-12 ${f.bg} rounded-2xl flex items-center justify-center mb-5`}>
                    <Icon className={`w-6 h-6 ${f.color}`} />
                  </div>
                  <h3 className="text-lg font-display font-bold text-gray-900 mb-2">{f.title}</h3>
                  <p className="text-gray-500 leading-relaxed text-sm">{f.desc}</p>
                </div>
              );
            })}
          </div>
        </div>
      </section>

      {/* How it works */}
      <section className="py-24 px-4 bg-white">
        <div className="max-w-5xl mx-auto">
          <div className="text-center mb-16">
            <p className="text-forest-600 font-semibold text-sm tracking-widest uppercase mb-3">Simple process</p>
            <h2 className="text-4xl font-display font-black text-gray-900">Start Improving in 3 Steps</h2>
          </div>
          <div className="grid grid-cols-1 md:grid-cols-3 gap-10">
            {STEPS.map((step, i) => (
              <div key={step.num} className="relative text-center">
                {i < STEPS.length - 1 && (
                  <div className="hidden md:block absolute top-10 left-[60%] w-full h-0.5 bg-gray-200" />
                )}
                <div className="w-20 h-20 bg-forest-600 rounded-3xl flex items-center justify-center mx-auto mb-6 shadow-lg relative z-10">
                  <span className="text-2xl font-display font-black text-white">{step.num}</span>
                </div>
                <h3 className="text-xl font-display font-bold text-gray-900 mb-3">{step.title}</h3>
                <p className="text-gray-500 leading-relaxed">{step.desc}</p>
              </div>
            ))}
          </div>
        </div>
      </section>

      {/* CTA */}
      <section className="py-24 px-4 bg-gradient-to-r from-forest-900 to-forest-700">
        <div className="max-w-3xl mx-auto text-center">
          <div className="w-16 h-16 bg-gold-500 rounded-3xl flex items-center justify-center mx-auto mb-8 shadow-xl">
            <Globe className="w-9 h-9 text-forest-900" />
          </div>
          <h2 className="text-4xl sm:text-5xl font-display font-black text-white mb-6">
            Ready to Ace Your KCSE?
          </h2>
          <p className="text-forest-200 text-xl mb-10 leading-relaxed">
            Join Kenyan students already studying smarter with SomaSmart.
          </p>
          <Link href="/register" className="inline-flex items-center gap-2 bg-gold-500 hover:bg-gold-400 text-forest-950 font-black text-xl px-10 py-5 rounded-2xl transition-all hover:shadow-2xl">
            Create My Free Account <ChevronRight className="w-6 h-6" />
          </Link>
        </div>
      </section>

      {/* Footer */}
      <footer className="bg-gray-950 text-gray-500 py-10 px-4">
        <div className="max-w-6xl mx-auto flex flex-col md:flex-row items-center justify-between gap-4">
          <div className="flex items-center gap-2">
            <div className="w-7 h-7 bg-forest-600 rounded-lg flex items-center justify-center">
              <BookOpen className="w-4 h-4 text-white" />
            </div>
            <span className="text-white font-display font-bold">SomaSmart</span>
          </div>
          <p className="text-sm">&#169; 2025 SomaSmart. Built for Kenyan Students</p>
          <div className="flex gap-5 text-sm">
            {["Privacy","Terms","Contact"].map((l) => (
              <Link key={l} href="#" className="hover:text-white transition-colors">{l}</Link>
            ))}
          </div>
        </div>
      </footer>
    </div>
  );
}
''')

# ── 5. app/(auth)/layout.tsx ──────────────────────────────────────────────────
write("app/(auth)/layout.tsx", '''import Link from "next/link";
import { BookOpen } from "lucide-react";

export default function AuthLayout({ children }: { children: React.ReactNode }) {
  return (
    <div className="min-h-screen bg-gradient-to-br from-forest-950 via-forest-900 to-forest-800 bg-kenya-pattern flex flex-col">
      <div className="p-6">
        <Link href="/" className="inline-flex items-center gap-2 group">
          <div className="w-9 h-9 bg-forest-600 rounded-xl flex items-center justify-center group-hover:bg-forest-500 transition-colors">
            <BookOpen className="w-5 h-5 text-white" />
          </div>
          <span className="text-xl font-display font-bold text-white">
            Soma<span className="text-gold-400">Smart</span>
          </span>
        </Link>
      </div>
      <div className="flex-1 flex items-center justify-center p-4">{children}</div>
      <div className="p-6 text-center text-forest-400 text-sm">
        &#169; 2025 SomaSmart &#8226; Built for Kenyan Students
      </div>
    </div>
  );
}
''')

# ── 6. app/(auth)/login/page.tsx ──────────────────────────────────────────────
write("app/(auth)/login/page.tsx", '''"use client";

import { useState } from "react";
import Link from "next/link";
import { Eye, EyeOff, Mail, Lock, AlertCircle } from "lucide-react";

const GoogleIcon = () => (
  <svg className="w-5 h-5 flex-shrink-0" viewBox="0 0 24 24">
    <path fill="#4285F4" d="M22.56 12.25c0-.78-.07-1.53-.2-2.25H12v4.26h5.92c-.26 1.37-1.04 2.53-2.21 3.31v2.77h3.57c2.08-1.92 3.28-4.74 3.28-8.09z"/>
    <path fill="#34A853" d="M12 23c2.97 0 5.46-.98 7.28-2.66l-3.57-2.77c-.98.66-2.23 1.06-3.71 1.06-2.86 0-5.29-1.93-6.16-4.53H2.18v2.84C3.99 20.53 7.7 23 12 23z"/>
    <path fill="#FBBC05" d="M5.84 14.09c-.22-.66-.35-1.36-.35-2.09s.13-1.43.35-2.09V7.07H2.18C1.43 8.55 1 10.22 1 12s.43 3.45 1.18 4.93l2.85-2.22.81-.62z"/>
    <path fill="#EA4335" d="M12 5.38c1.62 0 3.06.56 4.21 1.64l3.15-3.15C17.45 2.09 14.97 1 12 1 7.7 1 3.99 3.47 2.18 7.07l3.66 2.84c.87-2.6 3.3-4.53 6.16-4.53z"/>
  </svg>
);

export default function LoginPage() {
  const [showPassword, setShowPassword] = useState(false);
  const [loading, setLoading]           = useState(false);
  const [error, setError]               = useState("");
  const [form, setForm] = useState({ email: "", password: "" });

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    setError("");
    setLoading(true);
    await new Promise((r) => setTimeout(r, 800));
    setLoading(false);
  };

  return (
    <div className="w-full max-w-[420px] animate-slide-up">
      <div className="bg-white rounded-2xl shadow-2xl p-8">
        <div className="text-center mb-8">
          <h1 className="text-3xl font-display font-black text-gray-900 mb-2">Welcome back</h1>
          <p className="text-gray-500 text-sm">Log in to continue your revision</p>
        </div>

        <button type="button" className="w-full flex items-center justify-center gap-3 py-3 px-4 border-2 border-gray-200 rounded-xl hover:bg-gray-50 transition-all font-semibold text-gray-700 mb-6">
          <GoogleIcon />Continue with Google
        </button>

        <div className="relative mb-6">
          <div className="absolute inset-0 flex items-center"><div className="w-full border-t border-gray-200" /></div>
          <div className="relative flex justify-center">
            <span className="px-4 bg-white text-gray-400 text-sm">or use email</span>
          </div>
        </div>

        {error && (
          <div className="flex items-center gap-2 bg-red-50 border border-red-200 text-red-700 px-4 py-3 rounded-xl mb-5 text-sm">
            <AlertCircle className="w-4 h-4 flex-shrink-0" />{error}
          </div>
        )}

        <form onSubmit={handleSubmit} className="space-y-5">
          <div>
            <label className="block text-sm font-semibold text-gray-700 mb-2">Email address</label>
            <div className="relative">
              <Mail className="absolute left-3.5 top-1/2 -translate-y-1/2 w-5 h-5 text-gray-400" />
              <input type="email" required placeholder="student@email.com"
                value={form.email} onChange={(e) => setForm({ ...form, email: e.target.value })}
                className="input-field pl-11" />
            </div>
          </div>

          <div>
            <div className="flex items-center justify-between mb-2">
              <label className="text-sm font-semibold text-gray-700">Password</label>
              <Link href="#" className="text-xs text-forest-600 hover:text-forest-700 font-medium">Forgot password?</Link>
            </div>
            <div className="relative">
              <Lock className="absolute left-3.5 top-1/2 -translate-y-1/2 w-5 h-5 text-gray-400" />
              <input type={showPassword ? "text" : "password"} required placeholder="Enter your password"
                value={form.password} onChange={(e) => setForm({ ...form, password: e.target.value })}
                className="input-field pl-11 pr-12" />
              <button type="button" onClick={() => setShowPassword(!showPassword)}
                className="absolute right-3.5 top-1/2 -translate-y-1/2 text-gray-400 hover:text-gray-600">
                {showPassword ? <EyeOff className="w-5 h-5" /> : <Eye className="w-5 h-5" />}
              </button>
            </div>
          </div>

          <button type="submit" disabled={loading} className="btn-primary w-full py-3.5 text-base">
            {loading ? (
              <span className="flex items-center gap-2">
                <svg className="animate-spin w-4 h-4" viewBox="0 0 24 24" fill="none">
                  <circle className="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" strokeWidth="4"/>
                  <path className="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4z"/>
                </svg>
                Logging in...
              </span>
            ) : "Log In"}
          </button>
        </form>

        <p className="text-center text-gray-500 text-sm mt-6">
          Don&#39;t have an account?{" "}
          <Link href="/register" className="text-forest-600 hover:text-forest-700 font-semibold">Sign up free</Link>
        </p>
      </div>
    </div>
  );
}
''')

# ── 7. app/(auth)/register/page.tsx ──────────────────────────────────────────
write("app/(auth)/register/page.tsx", '''"use client";

import { useState } from "react";
import Link from "next/link";
import { Eye, EyeOff, Mail, Lock, User } from "lucide-react";

const SUBJECTS = [
  "Mathematics","English","Kiswahili","Biology","Chemistry","Physics",
  "Geography","History & Government","CRE","IRE","Home Science",
  "Computer Studies","Business Studies","Agriculture",
];

const GRADES = [
  { value:"form1", label:"Form 1" },{ value:"form2", label:"Form 2" },
  { value:"form3", label:"Form 3" },{ value:"form4", label:"Form 4 (KCSE)" },
  { value:"grade7",label:"Grade 7 (CBC)" },{ value:"grade8",label:"Grade 8 (CBC)" },
  { value:"grade9",label:"Grade 9 (CBC)" },
];

const GoogleIcon = () => (
  <svg className="w-5 h-5 flex-shrink-0" viewBox="0 0 24 24">
    <path fill="#4285F4" d="M22.56 12.25c0-.78-.07-1.53-.2-2.25H12v4.26h5.92c-.26 1.37-1.04 2.53-2.21 3.31v2.77h3.57c2.08-1.92 3.28-4.74 3.28-8.09z"/>
    <path fill="#34A853" d="M12 23c2.97 0 5.46-.98 7.28-2.66l-3.57-2.77c-.98.66-2.23 1.06-3.71 1.06-2.86 0-5.29-1.93-6.16-4.53H2.18v2.84C3.99 20.53 7.7 23 12 23z"/>
    <path fill="#FBBC05" d="M5.84 14.09c-.22-.66-.35-1.36-.35-2.09s.13-1.43.35-2.09V7.07H2.18C1.43 8.55 1 10.22 1 12s.43 3.45 1.18 4.93l2.85-2.22.81-.62z"/>
    <path fill="#EA4335" d="M12 5.38c1.62 0 3.06.56 4.21 1.64l3.15-3.15C17.45 2.09 14.97 1 12 1 7.7 1 3.99 3.47 2.18 7.07l3.66 2.84c.87-2.6 3.3-4.53 6.16-4.53z"/>
  </svg>
);

export default function RegisterPage() {
  const [step, setStep]                 = useState(1);
  const [showPassword, setShowPassword] = useState(false);
  const [loading, setLoading]           = useState(false);
  const [form, setForm] = useState({ fullName:"", email:"", password:"", grade:"", subjects:[] as string[] });

  const toggleSubject = (s: string) =>
    setForm((p) => ({ ...p, subjects: p.subjects.includes(s) ? p.subjects.filter((x) => x !== s) : [...p.subjects, s] }));

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    if (step === 1) { setStep(2); return; }
    setLoading(true);
    await new Promise((r) => setTimeout(r, 1000));
    setLoading(false);
  };

  return (
    <div className="w-full max-w-[440px] animate-slide-up">
      <div className="bg-white rounded-2xl shadow-2xl p-8">

        <div className="flex gap-2 mb-8">
          <div className={`h-1.5 flex-1 rounded-full transition-colors duration-300 ${step >= 1 ? "bg-forest-600" : "bg-gray-200"}`} />
          <div className={`h-1.5 flex-1 rounded-full transition-colors duration-300 ${step >= 2 ? "bg-forest-600" : "bg-gray-200"}`} />
        </div>

        <div className="text-center mb-8">
          <h1 className="text-3xl font-display font-black text-gray-900 mb-2">
            {step === 1 ? "Create Your Account" : "Personalise Learning"}
          </h1>
          <p className="text-gray-500 text-sm">
            {step === 1 ? "Step 1 of 2 — Account details" : "Step 2 of 2 — Your subjects"}
          </p>
        </div>

        {step === 1 && (
          <>
            <button type="button" className="w-full flex items-center justify-center gap-3 py-3 px-4 border-2 border-gray-200 rounded-xl hover:bg-gray-50 transition-all font-semibold text-gray-700 mb-6">
              <GoogleIcon />Sign up with Google
            </button>
            <div className="relative mb-6">
              <div className="absolute inset-0 flex items-center"><div className="w-full border-t border-gray-200" /></div>
              <div className="relative flex justify-center">
                <span className="px-4 bg-white text-gray-400 text-sm">or use email</span>
              </div>
            </div>
          </>
        )}

        <form onSubmit={handleSubmit} className="space-y-5">
          {step === 1 ? (
            <>
              <div>
                <label className="block text-sm font-semibold text-gray-700 mb-2">Full Name</label>
                <div className="relative">
                  <User className="absolute left-3.5 top-1/2 -translate-y-1/2 w-5 h-5 text-gray-400" />
                  <input type="text" required placeholder="e.g. Amina Wanjiku" value={form.fullName}
                    onChange={(e) => setForm({ ...form, fullName: e.target.value })} className="input-field pl-11" />
                </div>
              </div>
              <div>
                <label className="block text-sm font-semibold text-gray-700 mb-2">Email Address</label>
                <div className="relative">
                  <Mail className="absolute left-3.5 top-1/2 -translate-y-1/2 w-5 h-5 text-gray-400" />
                  <input type="email" required placeholder="student@email.com" value={form.email}
                    onChange={(e) => setForm({ ...form, email: e.target.value })} className="input-field pl-11" />
                </div>
              </div>
              <div>
                <label className="block text-sm font-semibold text-gray-700 mb-2">Password</label>
                <div className="relative">
                  <Lock className="absolute left-3.5 top-1/2 -translate-y-1/2 w-5 h-5 text-gray-400" />
                  <input type={showPassword ? "text" : "password"} required placeholder="Min. 8 characters"
                    value={form.password} onChange={(e) => setForm({ ...form, password: e.target.value })}
                    className="input-field pl-11 pr-12" />
                  <button type="button" onClick={() => setShowPassword(!showPassword)}
                    className="absolute right-3.5 top-1/2 -translate-y-1/2 text-gray-400 hover:text-gray-600">
                    {showPassword ? <EyeOff className="w-5 h-5" /> : <Eye className="w-5 h-5" />}
                  </button>
                </div>
              </div>
            </>
          ) : (
            <>
              <div>
                <label className="block text-sm font-semibold text-gray-700 mb-2">Grade / Form</label>
                <select required value={form.grade} onChange={(e) => setForm({ ...form, grade: e.target.value })}
                  className="input-field bg-white">
                  <option value="">Select your grade</option>
                  {GRADES.map((g) => <option key={g.value} value={g.value}>{g.label}</option>)}
                </select>
              </div>
              <div>
                <label className="block text-sm font-semibold text-gray-700 mb-3">
                  Your Subjects
                  <span className="text-gray-400 font-normal ml-2 text-xs">({form.subjects.length} selected)</span>
                </label>
                <div className="grid grid-cols-2 gap-2 max-h-48 overflow-y-auto pr-1">
                  {SUBJECTS.map((s) => {
                    const on = form.subjects.includes(s);
                    return (
                      <button key={s} type="button" onClick={() => toggleSubject(s)}
                        className={`text-left px-3 py-2 rounded-xl text-sm font-medium border-2 transition-all ${on ? "bg-forest-50 border-forest-500 text-forest-700" : "bg-white border-gray-200 text-gray-600 hover:border-gray-300"}`}>
                        {on ? "✓ " : ""}{s}
                      </button>
                    );
                  })}
                </div>
              </div>
            </>
          )}

          <button type="submit" disabled={loading} className="btn-primary w-full py-3.5 text-base">
            {loading ? "Creating Account..." : step === 1 ? "Continue →" : "Start Learning Free 🚀"}
          </button>
        </form>

        {step === 1 && (
          <p className="text-center text-gray-500 text-sm mt-6">
            Already have an account?{" "}
            <Link href="/login" className="text-forest-600 hover:text-forest-700 font-semibold">Log in</Link>
          </p>
        )}
        {step === 2 && (
          <button onClick={() => setStep(1)}
            className="w-full text-center text-sm text-gray-400 hover:text-gray-600 mt-4 transition-colors">
            ← Back to account details
          </button>
        )}
      </div>
    </div>
  );
}
''')

# ── 8. app/(dashboard)/layout.tsx ────────────────────────────────────────────
write("app/(dashboard)/layout.tsx", '''"use client";

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
''')

# ── 9. app/(dashboard)/dashboard/page.tsx ────────────────────────────────────
write("app/(dashboard)/dashboard/page.tsx", '''import Link from "next/link";
import {
  MessageSquare, HelpCircle, Upload, Clock,
  TrendingUp, ChevronRight, Flame, BookOpen, ArrowUpRight, AlertCircle,
} from "lucide-react";

const ACTIONS = [
  { href:"/chat",     icon:MessageSquare, label:"Ask AI Tutor", desc:"Get instant explanations", iconColor:"text-forest-600", iconBg:"bg-forest-50" },
  { href:"/quiz",     icon:HelpCircle,    label:"Take a Quiz",  desc:"Test your knowledge",      iconColor:"text-blue-600",   iconBg:"bg-blue-50"   },
  { href:"/upload",   icon:Upload,        label:"Upload Paper", desc:"PDF or image analysis",    iconColor:"text-purple-600", iconBg:"bg-purple-50" },
  { href:"/schedule", icon:Clock,         label:"My Schedule",  desc:"View revision plan",       iconColor:"text-amber-600",  iconBg:"bg-amber-50"  },
];

const SCORES = [
  { name:"Mathematics", topic:"Quadratic Equations", score:72, bar:"bg-blue-500"    },
  { name:"Chemistry",   topic:"Acids & Bases",        score:58, bar:"bg-green-500"   },
  { name:"Biology",     topic:"Cell Division",         score:85, bar:"bg-emerald-500" },
  { name:"English",     topic:"Essay Writing",          score:67, bar:"bg-purple-500"  },
];

const WEAK = [
  { subject:"Chemistry",   topic:"Electrochemistry", priority:"high"   },
  { subject:"Mathematics", topic:"Trigonometry",     priority:"high"   },
  { subject:"Biology",     topic:"Genetics",          priority:"medium" },
];

const RECENT = [
  { subject:"Mathematics", time:"2 hours ago", type:"Chat"   },
  { subject:"Chemistry",   time:"Yesterday",   type:"Quiz"   },
  { subject:"English",     time:"2 days ago",  type:"Upload" },
];

const TODAY = [
  { time:"8:00 AM",  subject:"Mathematics", topic:"Quadratic Equations", done:true  },
  { time:"10:00 AM", subject:"Chemistry",   topic:"Electrochemistry",    done:false },
  { time:"2:00 PM",  subject:"English",     topic:"Essay Writing",        done:false },
];

export default function DashboardPage() {
  return (
    <div className="space-y-6 max-w-6xl mx-auto animate-fade-in">

      {/* Banner */}
      <div className="bg-gradient-to-r from-forest-900 to-forest-700 rounded-2xl p-6 sm:p-8 text-white relative overflow-hidden">
        <div className="absolute top-0 right-0 w-64 h-64 bg-forest-600/20 rounded-full -translate-y-1/2 translate-x-1/4 pointer-events-none" />
        <div className="relative flex items-center justify-between flex-wrap gap-4">
          <div>
            <p className="text-forest-300 text-sm font-medium">Good morning 👋</p>
            <h2 className="text-2xl sm:text-3xl font-display font-black mt-1 mb-1">Ready to study, Student?</h2>
            <p className="text-forest-200 text-sm">3 topics scheduled today</p>
          </div>
          <div className="flex items-center gap-6">
            <div className="text-center">
              <div className="flex items-center gap-1.5 text-3xl font-display font-black text-gold-400">
                <Flame className="w-7 h-7" />7
              </div>
              <p className="text-forest-300 text-xs mt-1">Day streak</p>
            </div>
            <div className="text-center">
              <div className="text-3xl font-display font-black">42</div>
              <p className="text-forest-300 text-xs mt-1">Sessions</p>
            </div>
          </div>
        </div>
      </div>

      {/* Quick actions */}
      <div>
        <h3 className="font-display font-bold text-gray-900 text-lg mb-4">Quick Actions</h3>
        <div className="grid grid-cols-2 lg:grid-cols-4 gap-4">
          {ACTIONS.map(({ href, icon: Icon, label, desc, iconColor, iconBg }) => (
            <Link key={href} href={href} className="card-hover p-5">
              <div className={`w-11 h-11 ${iconBg} rounded-xl flex items-center justify-center mb-4`}>
                <Icon className={`w-6 h-6 ${iconColor}`} />
              </div>
              <p className="font-bold text-gray-900 text-sm">{label}</p>
              <p className="text-gray-500 text-xs mt-1">{desc}</p>
            </Link>
          ))}
        </div>
      </div>

      {/* Performance + Focus */}
      <div className="grid grid-cols-1 lg:grid-cols-3 gap-6">
        <div className="lg:col-span-2 card p-6">
          <div className="flex items-center justify-between mb-6">
            <div className="flex items-center gap-2">
              <TrendingUp className="w-5 h-5 text-forest-600" />
              <h3 className="font-display font-bold text-gray-900">Subject Performance</h3>
            </div>
            <Link href="/progress" className="flex items-center gap-1 text-forest-600 text-sm font-semibold">
              Full report <ArrowUpRight className="w-4 h-4" />
            </Link>
          </div>
          <div className="space-y-5">
            {SCORES.map((s) => (
              <div key={s.name}>
                <div className="flex items-center justify-between mb-1.5">
                  <div className="flex items-center gap-2">
                    <span className="font-semibold text-gray-900 text-sm">{s.name}</span>
                    <span className="text-gray-400 text-xs hidden sm:block">&#8226; {s.topic}</span>
                  </div>
                  <span className="text-sm font-bold text-gray-700">{s.score}%</span>
                </div>
                <div className="w-full bg-gray-100 rounded-full h-2">
                  <div className={`h-2 rounded-full ${s.bar} transition-all duration-500`} style={{ width:`${s.score}%` }} />
                </div>
              </div>
            ))}
          </div>
        </div>

        <div className="card p-6">
          <div className="flex items-center gap-2 mb-6">
            <AlertCircle className="w-5 h-5 text-amber-500" />
            <h3 className="font-display font-bold text-gray-900">Focus Areas</h3>
          </div>
          <div className="space-y-3">
            {WEAK.map((w) => (
              <div key={w.topic} className="flex items-center justify-between p-3 bg-gray-50 rounded-xl">
                <div>
                  <p className="text-sm font-semibold text-gray-900">{w.topic}</p>
                  <p className="text-xs text-gray-500">{w.subject}</p>
                </div>
                <span className={`badge ${w.priority === "high" ? "badge-red" : "badge-gold"}`}>{w.priority}</span>
              </div>
            ))}
          </div>
          <Link href="/chat" className="btn-primary w-full mt-5 text-sm py-2.5">
            Study Weak Topics
          </Link>
        </div>
      </div>

      {/* Recent + Schedule */}
      <div className="grid grid-cols-1 lg:grid-cols-2 gap-6">
        <div className="card p-6">
          <div className="flex items-center justify-between mb-5">
            <h3 className="font-display font-bold text-gray-900">Recent Activity</h3>
            <Link href="/progress" className="text-forest-600 text-sm font-semibold">View all</Link>
          </div>
          <div className="space-y-3">
            {RECENT.map((r, i) => (
              <div key={i} className="flex items-center gap-3 p-3 bg-gray-50 rounded-xl">
                <div className="w-9 h-9 bg-forest-100 rounded-xl flex items-center justify-center">
                  <BookOpen className="w-4 h-4 text-forest-600" />
                </div>
                <div className="flex-1 min-w-0">
                  <p className="text-sm font-semibold text-gray-900">{r.subject}</p>
                  <p className="text-xs text-gray-500">{r.type} &#8226; {r.time}</p>
                </div>
                <ChevronRight className="w-4 h-4 text-gray-300" />
              </div>
            ))}
          </div>
        </div>

        <div className="card p-6">
          <div className="flex items-center justify-between mb-5">
            <h3 className="font-display font-bold text-gray-900">{"Today's Schedule"}</h3>
            <Link href="/schedule" className="text-forest-600 text-sm font-semibold">Full plan</Link>
          </div>
          <div className="space-y-3">
            {TODAY.map((t, i) => (
              <div key={i} className={`flex items-center gap-3 p-3 rounded-xl ${t.done ? "bg-forest-50 border border-forest-100" : "bg-gray-50"}`}>
                <div className={`w-2 h-2 rounded-full flex-shrink-0 ${t.done ? "bg-forest-500" : "bg-amber-400"}`} />
                <div className="flex-1 min-w-0">
                  <p className="text-sm font-semibold text-gray-900">{t.subject}</p>
                  <p className="text-xs text-gray-500">{t.topic}</p>
                </div>
                <span className="text-xs text-gray-400 whitespace-nowrap">{t.time}</span>
              </div>
            ))}
          </div>
        </div>
      </div>
    </div>
  );
}
''')

# ── Placeholder pages ─────────────────────────────────────────────────────────
PLACEHOLDERS = [
  ("app/(dashboard)/chat/page.tsx",     "MessageSquare", "AI Tutor Chat",     "Full AI chat powered by Groq",     "text-forest-600", "bg-forest-50" ),
  ("app/(dashboard)/quiz/page.tsx",     "HelpCircle",    "Quiz Generator",    "Auto-generated KCSE-style quizzes","text-blue-600",   "bg-blue-50"   ),
  ("app/(dashboard)/progress/page.tsx", "BarChart2",     "Progress Tracker",  "Detailed subject analytics",       "text-purple-600", "bg-purple-50" ),
  ("app/(dashboard)/schedule/page.tsx", "Calendar",      "Revision Schedule", "Personalised revision timetable",  "text-amber-600",  "bg-amber-50"  ),
  ("app/(dashboard)/upload/page.tsx",   "Upload",        "Upload Materials",  "PDF and image analysis",           "text-pink-600",   "bg-pink-50"   ),
]

for (path, icon, title, desc, color, bg) in PLACEHOLDERS:
    write(path, f'''"use client";
import {{ {icon} }} from "lucide-react";
export default function Page() {{
  return (
    <div className="flex items-center justify-center h-[60vh]">
      <div className="text-center">
        <div className="w-16 h-16 {bg} rounded-2xl flex items-center justify-center mx-auto mb-4">
          <{icon} className="w-8 h-8 {color}" />
        </div>
        <h2 className="text-2xl font-display font-bold text-gray-900 mb-2">{title}</h2>
        <p className="text-gray-400">{desc}</p>
      </div>
    </div>
  );
}}
''')

# ── lib/utils.ts ──────────────────────────────────────────────────────────────
write("lib/utils.ts", '''import { clsx, type ClassValue } from "clsx";
import { twMerge } from "tailwind-merge";

export function cn(...inputs: ClassValue[]) {
  return twMerge(clsx(inputs));
}
''')

# ── types/index.ts ────────────────────────────────────────────────────────────
write("types/index.ts", '''export interface User {
  id: string;
  email: string;
  full_name: string;
  grade: string;
  subjects: string[];
  created_at: string;
}

export interface Message {
  id: string;
  role: "user" | "assistant";
  content: string;
  created_at: string;
}

export interface ChatSession {
  id: string;
  user_id: string;
  subject: string;
  messages: Message[];
  created_at: string;
}

export interface WeakTopic {
  subject: string;
  topic: string;
  score: number;
  priority: "high" | "medium" | "low";
}

export interface ScheduleItem {
  id: string;
  subject: string;
  topic: string;
  scheduled_time: string;
  duration_minutes: number;
  completed: boolean;
}
''')

print()
print("All 16 files created successfully!")
print()
print("Next steps:")
print("  1.  pnpm add lucide-react clsx tailwind-merge   (if not done)")
print("  2.  pnpm dev")
print("  3.  Open http://localhost:3000")
