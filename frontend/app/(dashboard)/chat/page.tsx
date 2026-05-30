"use client";
import { MessageSquare } from "lucide-react";
export default function Page() {
  return (
    <div className="flex items-center justify-center h-[60vh]">
      <div className="text-center">
        <div className="w-16 h-16 bg-forest-50 rounded-2xl flex items-center justify-center mx-auto mb-4">
          <MessageSquare className="w-8 h-8 text-forest-600" />
        </div>
        <h2 className="text-2xl font-display font-bold text-gray-900 mb-2">AI Tutor Chat</h2>
        <p className="text-gray-400">Full AI chat powered by Groq</p>
      </div>
    </div>
  );
}
