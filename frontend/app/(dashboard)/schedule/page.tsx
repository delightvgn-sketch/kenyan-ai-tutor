"use client";
import { Calendar } from "lucide-react";
export default function Page() {
  return (
    <div className="flex items-center justify-center h-[60vh]">
      <div className="text-center">
        <div className="w-16 h-16 bg-amber-50 rounded-2xl flex items-center justify-center mx-auto mb-4">
          <Calendar className="w-8 h-8 text-amber-600" />
        </div>
        <h2 className="text-2xl font-display font-bold text-gray-900 mb-2">Revision Schedule</h2>
        <p className="text-gray-400">Personalised revision timetable</p>
      </div>
    </div>
  );
}
