module.exports = function (eleventyConfig) {
  // Passthrough copy for static assets
  eleventyConfig.addPassthroughCopy("src/assets");

  // Add a filter to get the corresponding page URL in another language
  eleventyConfig.addFilter("otherLangUrl", function (url, currentLang) {
    if (currentLang === "ko") {
      return url.replace(/^\/ko\//, "/en/");
    } else {
      return url.replace(/^\/en\//, "/ko/");
    }
  });

  // Add a filter for date formatting
  eleventyConfig.addFilter("dateFormat", function (date, lang) {
    if (!date) return "";
    const d = new Date(date);
    if (lang === "ko") {
      return `${d.getFullYear()}년 ${d.getMonth() + 1}월`;
    }
    const months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun",
      "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"];
    return `${months[d.getMonth()]} ${d.getFullYear()}`;
  });

  return {
    dir: {
      input: "src",
      output: "_site",
      includes: "_includes",
      data: "_data",
    },
    templateFormats: ["md", "njk", "html"],
    markdownTemplateEngine: "njk",
    htmlTemplateEngine: "njk",
  };
};
