import Link from "next/link";
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
