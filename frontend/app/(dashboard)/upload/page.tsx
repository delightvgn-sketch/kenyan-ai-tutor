"use client";
import { Upload } from "lucide-react";
export default function Page() {
  return (
    <div className="flex items-center justify-center h-[60vh]">
      <div className="text-center">
        <div className="w-16 h-16 bg-pink-50 rounded-2xl flex items-center justify-center mx-auto mb-4">
          <Upload className="w-8 h-8 text-pink-600" />
        </div>
        <h2 className="text-2xl font-display font-bold text-gray-900 mb-2">Upload Materials</h2>
        <p className="text-gray-400">PDF and image analysis</p>
      </div>
    </div>
  );
}
