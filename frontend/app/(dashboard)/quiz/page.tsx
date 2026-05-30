"use client";
import { HelpCircle } from "lucide-react";
export default function Page() {
  return (
    <div className="flex items-center justify-center h-[60vh]">
      <div className="text-center">
        <div className="w-16 h-16 bg-blue-50 rounded-2xl flex items-center justify-center mx-auto mb-4">
          <HelpCircle className="w-8 h-8 text-blue-600" />
        </div>
        <h2 className="text-2xl font-display font-bold text-gray-900 mb-2">Quiz Generator</h2>
        <p className="text-gray-400">Auto-generated KCSE-style quizzes</p>
      </div>
    </div>
  );
}
