import type { Metadata } from "next";
import "./globals.css";

export const metadata: Metadata = {
  title: "ClearCare - Find Hospitals Near You",
  description: "Instantly find hospitals and healthcare facilities near your location. Search by ZIP code and get real-time results with ratings and availability.",
  keywords: "hospitals, healthcare, medical facilities, hospital finder, healthcare search, emergency room, urgent care",
  openGraph: {
    title: "ClearCare - Find Hospitals Near You",
    description: "Instantly find hospitals and healthcare facilities near your location.",
    type: "website",
  },
};

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <html lang="en">
      <body className="antialiased">
        {children}
      </body>
    </html>
  );
}
