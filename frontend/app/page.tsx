import ChatInterface from "./components/ChatInterface";

export default function Home() {
  return (
    <main className="min-h-screen bg-gray-100 flex items-center justify-center">
      <div className="w-full h-screen md:h-[85vh] md:max-w-2xl bg-white md:rounded-2xl md:shadow-2xl overflow-hidden relative">
        <ChatInterface />
      </div>
    </main>
  );
}
