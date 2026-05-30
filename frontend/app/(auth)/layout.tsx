import Link from "next/link";
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
