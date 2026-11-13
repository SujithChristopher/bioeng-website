export interface NewsItem {
  title: string;
  description: string;
  image?: string;
  date?: string; // display string, e.g. "Oct 31, 2026"
}

// Single source of truth for news. Newest first.
export const newsItems: NewsItem[] = [
  {
    title: "Farewell and Best Wishes to Monisha!",
    date: "Oct 31, 2026",
    description:
      "We are excited to announce that our student Dr. Monisha will begin her postdoctoral research at the Shirley Ryan AbilityLab. She will work with Dr. Milap Sandhu to study motor control in multiple sclerosis using high density EMG decomposition. We wish Monisha all the best in her new role!",
  },
  {
    title: "16th Annual Research Day Awards, CMC Vellore",
    date: "Oct 6, 2026",
    description:
      "Congratulations to Neelakshi Ganguly, Parvathy Neelakandan, Pooja Vinayagamoorthy and Sujith Christopher for poster presentation awards at the 16th Annual Research day at CMC Vellore.",
  },
  {
    title: "VIT - BioMET'26 Awards",
    date: "Aug 7, 2026",
    description:
      "Congratulations to Neelakshi Ganguly for winning the VIT Three Minute Presentation Award and Sujith Christopher for winning the VIT Best E-Poster Presentation Award at the International Conference on Biomaterials, Bioengineering and Biotheranostics (BioMET'26) held during August 5-7, 2026 in Vellore.",
  },
  {
    title: "IFNR Annual Conference Awards",
    date: "April 12, 2026",
    description:
      "Congratulations to Neelakshi Ganguly and Sujith Christopher for winning E-poster Competition awards and Charles Jebaraj for Travel Bursary at the 2nd International Tele Neuro Rehabilitation Conference (ITNRCON 2026) & 14th Annual Conference of IFNR (IFNRCON2026) held during April 9-12, 2026 in Mumbai.",
  },
  {
    title: "NOARK: Not Just an Arm Skateboard",
    date: "Feb 5, 2026",
    description:
      "Introducing NOARK — a portable, gamified arm skateboard designed for upper-limb rehabilitation, making therapy engaging and accessible for patients.",
    image: "/news/noark_news.jpg",
  },
  {
    title: "PLUTO - A Portable Plug-and-Play Robot",
    date: "Jan 17, 2025",
    description:
      "Our research team has developed PLUTO, a portable plug-and-play robot. PLUTO provides targeted therapy for wrist and hand movement using a single actuator and a set of interchangeable mechanical handles.",
    image: "/news/pluto_news1.png",
  },
  {
    title: "Research Day 2024",
    description:
      "BioRehab Group participated in the annual research day, showcasing our latest developments in neurorehabilitation technologies and collaborative research initiatives.",
    image: "/news/pluto_news2.png",
  },
];
