"use client";

import { motion } from "framer-motion";
import { useState, useEffect } from "react";
import Image from "next/image";

type CharacterProps = {
    emotion: string; // "neutral", "warm", "serious", "thinking", etc.
    strengthLevel: number; // 1, 2, 3
};

export default function CharacterDisplay({ emotion, strengthLevel }: CharacterProps) {
    // 画像パスの決定ロジック
    // 画像ファイル名は実装時に調整してください。現在はプレースホルダーです。
    const getImagePath = () => {
        // ローディング中の思考ポーズ
        if (emotion === "thinking") return "/characters/thinking.png";

        // エラー時
        if (emotion === "sad") return "/characters/error.png";

        // 強度（性格）ごとの画像分岐
        switch (strengthLevel) {
            case 1: // 共感コーチ
                return emotion === "warm" ? "/characters/warm_smile.png" : "/characters/warm_base.png";
            case 2: // 戦略コンサル
                return emotion === "neutral" ? "/characters/logical_base.png" : "/characters/logical_explain.png";
            case 3: // 鬼軍曹
                return emotion === "serious" ? "/characters/strict_anger.png" : "/characters/strict_base.png";
            default:
                return "/characters/warm_base.png";
        }
    };

    const imagePath = getImagePath();

    return (
        <div className="relative w-64 h-64 mx-auto my-4">
            {/* 背景のエフェクト（感情に合わせて色が変わる） */}
            <motion.div
                className={`absolute inset-0 rounded-full blur-2xl opacity-50 
          ${emotion === "warm" ? "bg-pink-300" : ""}
          ${emotion === "serious" ? "bg-red-500" : ""}
          ${emotion === "neutral" ? "bg-blue-300" : ""}
          ${emotion === "thinking" ? "bg-yellow-200 animate-pulse" : ""}
        `}
                animate={{ scale: [1, 1.1, 1] }}
                transition={{ duration: 2, repeat: Infinity }}
            />

            {/* キャラクター画像 */}
            <motion.div
                key={imagePath} // Keyが変わるとアニメーションが再発火する
                initial={{ opacity: 0, scale: 0.9 }}
                animate={{ opacity: 1, scale: 1 }}
                transition={{ duration: 0.3 }}
                className="relative z-10"
            >
                {/* Next.js Image optimization (本来はwidth/height必須ですが、一旦fillで対応も可) */}
                {/* ここではモック用に単なるdivとimgタグを使いますが、本番はnext/image推奨 */}
                <img
                    src={imagePath}
                    alt="Character"
                    className="w-full h-full object-contain drop-shadow-lg"
                    onError={(e) => {
                        // 画像がない場合のフォールバック（デバッグ用）
                        e.currentTarget.src = "https://placehold.co/400x400?text=No+Image";
                    }}
                />
            </motion.div>
        </div>
    );
}
