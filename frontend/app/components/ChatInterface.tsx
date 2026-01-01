"use client";

import { useState } from "react";
import axios from "axios";
import { Send, User, Bot, Sparkles } from "lucide-react";
import CharacterDisplay from "@/components/ui/CharacterDisplay";

// チャットメッセージの型定義
type Message = {
    role: "user" | "model";
    content: string;
};

export default function ChatInterface() {
    const [input, setInput] = useState("");
    const [messages, setMessages] = useState<Message[]>([]);
    const [isLoading, setIsLoading] = useState(false);

    // 現在のモードと感情状態
    const [strengthLevel, setStrengthLevel] = useState(1);
    const [currentEmotion, setCurrentEmotion] = useState("neutral");

    const sendMessage = async () => {
        if (!input.trim()) return;

        const userMessage: Message = { role: "user", content: input };
        setMessages((prev) => [...prev, userMessage]);
        setInput("");
        setIsLoading(true);
        setCurrentEmotion("thinking"); // 思考中モードへ

        try {
            // APIリクエスト
            // 注意: バックエンドのURLは環境変数に入れるべきですが、一旦直書き
            const res = await axios.post("http://127.0.0.1:8000/api/chat/", {
                message: userMessage.content,
                history: messages, // 過去ログも送る
                strength_level: strengthLevel,
            });

            const aiData = res.data;
            const aiMessage: Message = { role: "model", content: aiData.response };

            setMessages((prev) => [...prev, aiMessage]);
            setCurrentEmotion(aiData.emotion); // AIの感情を反映

        } catch (error) {
            console.error("Error:", error);
            setCurrentEmotion("sad"); // エラー時の表情
            setMessages((prev) => [...prev, { role: "model", content: "エラーが発生しました。もう一度お試しください。" }]);
        } finally {
            setIsLoading(false);
        }
    };

    return (
        <div className="flex flex-col h-full max-w-2xl mx-auto bg-gray-50 shadow-xl overflow-hidden font-sans text-gray-800">
            {/* Header & Mode Selector */}
            <div className="p-4 bg-white border-b border-gray-200 flex justify-between items-center z-20">
                <h1 className="text-xl font-bold bg-gradient-to-r from-purple-600 to-blue-500 bg-clip-text text-transparent">
                    Resolution Mate
                </h1>
                <select
                    value={strengthLevel}
                    onChange={(e) => setStrengthLevel(Number(e.target.value))}
                    className="p-2 border rounded-lg text-sm bg-gray-100 hover:bg-gray-200 transition-colors focus:ring-2 focus:ring-purple-500 outline-none"
                >
                    <option value={1}>Lv.1 ライフコーチ (Warm)</option>
                    <option value={2}>Lv.2 戦略コンサル (Logical)</option>
                    <option value={3}>Lv.3 実行パートナー (Strict)</option>
                </select>
            </div>

            {/* Character Area (固定表示) */}
            <div className="bg-gradient-to-b from-white to-gray-50 pt-4 pb-2 shrink-0 z-10">
                <CharacterDisplay emotion={currentEmotion} strengthLevel={strengthLevel} />
            </div>

            {/* Chat History Area (スクロール) */}
            <div className="flex-1 overflow-y-auto p-4 space-y-4 bg-gray-50 min-h-0">
                {messages.length === 0 && (
                    <div className="text-center text-gray-400 mt-10">
                        <Sparkles className="w-12 h-12 mx-auto mb-2 opacity-50" />
                        <p>新年の抱負を話してください。<br />私がサポートします。</p>
                    </div>
                )}

                {messages.map((msg, idx) => (
                    <div
                        key={idx}
                        className={`flex ${msg.role === "user" ? "justify-end" : "justify-start"}`}
                    >
                        <div
                            className={`max-w-[80%] p-4 rounded-2xl shadow-sm text-sm leading-relaxed whitespace-pre-wrap
                ${msg.role === "user"
                                    ? "bg-purple-600 text-white rounded-tr-none"
                                    : "bg-white border border-gray-100 text-gray-800 rounded-tl-none"
                                }`}
                        >
                            {msg.content}
                        </div>
                    </div>
                ))}

                {/* Loading Indicator */}
                {isLoading && (
                    <div className="flex justify-start">
                        <div className="bg-gray-200 text-gray-500 p-3 rounded-2xl rounded-tl-none text-xs animate-pulse">
                            AI is thinking...
                        </div>
                    </div>
                )}
            </div>

            {/* Input Area */}
            <div className="p-4 bg-white border-t border-gray-200 shrink-0">
                <div className="flex gap-2">
                    <input
                        type="text"
                        className="flex-1 p-3 border border-gray-300 rounded-xl focus:outline-none focus:ring-2 focus:ring-purple-500 transition-all shadow-inner"
                        placeholder="ここにメッセージを入力..."
                        value={input}
                        onChange={(e) => setInput(e.target.value)}
                        onKeyDown={(e) => e.key === "Enter" && !e.nativeEvent.isComposing && sendMessage()} // 日本語変換確定のEnter除外
                    />
                    <button
                        onClick={sendMessage}
                        disabled={isLoading || !input.trim()}
                        className="p-3 bg-purple-600 text-white rounded-xl hover:bg-purple-700 disabled:opacity-50 disabled:cursor-not-allowed transition-all shadow-md active:scale-95"
                    >
                        <Send size={20} />
                    </button>
                </div>
            </div>
        </div>
    );
}
