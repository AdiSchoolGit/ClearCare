'use client';

import SearchBox from './SearchBox';

export default function Hero() {
  return (
    <section className="pt-28 pb-16 lg:pt-36 lg:pb-24 bg-gradient-to-b from-primary-50/30 to-white">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div className="text-center max-w-4xl mx-auto">
          {/* Badge */}
          <div className="inline-flex items-center px-4 py-1.5 bg-secondary-100 text-secondary-700 rounded-full text-sm font-medium mb-6">
            <span className="w-2 h-2 bg-secondary-500 rounded-full mr-2 animate-pulse-soft"></span>
            Take control of your healthcare costs
          </div>

          {/* Main Headline */}
          <h1 className="text-4xl sm:text-5xl lg:text-6xl font-bold text-neutral-900 tracking-tight mb-6">
            Find the best value care,{' '}
            <span className="bg-gradient-to-r from-primary-500 to-primary-600 bg-clip-text text-transparent">for you</span>
          </h1>

          {/* Subheadline */}
          <p className="text-lg sm:text-xl text-neutral-600 mb-10 max-w-2xl mx-auto leading-relaxed">
            Compare healthcare costs based on your insurance, procedure type, and location.
            Whether you're insured or not, find affordable care that fits your needs.
          </p>

          {/* Search Box */}
          <div id="search" className="mb-8">
            <SearchBox />
          </div>

          {/* Trust Indicators */}
          <div className="flex flex-wrap justify-center items-center gap-6 text-sm text-neutral-500">
            <div className="flex items-center">
              <svg className="w-5 h-5 text-secondary-500 mr-2" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M5 13l4 4L19 7" />
              </svg>
              Free to use
            </div>
            <div className="flex items-center">
              <svg className="w-5 h-5 text-secondary-500 mr-2" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M5 13l4 4L19 7" />
              </svg>
              Insurance-aware pricing
            </div>
            <div className="flex items-center">
              <svg className="w-5 h-5 text-secondary-500 mr-2" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M5 13l4 4L19 7" />
              </svg>
              Nationwide coverage
            </div>
          </div>
        </div>
      </div>
    </section>
  );
}
