import Link from "next/link";
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
