"use client";
import { BarChart2 } from "lucide-react";
export default function Page() {
  return (
    <div className="flex items-center justify-center h-[60vh]">
      <div className="text-center">
        <div className="w-16 h-16 bg-purple-50 rounded-2xl flex items-center justify-center mx-auto mb-4">
          <BarChart2 className="w-8 h-8 text-purple-600" />
        </div>
        <h2 className="text-2xl font-display font-bold text-gray-900 mb-2">Progress Tracker</h2>
        <p className="text-gray-400">Detailed subject analytics</p>
      </div>
    </div>
  );
}
