export interface User {
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
