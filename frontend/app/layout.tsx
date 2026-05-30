import type { Metadata } from "next";
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
