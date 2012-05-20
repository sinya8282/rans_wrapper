class compile {
 public:
  compile(const std::string&);
  ~compile();
  std::string val(const std::string&);
  std::string rep(const std::string&);
  std::string compress(const std::string&);
  std::string decompress(const std::string&);
  bool accept(const std::string&);
  unsigned int size();
private:
  void* self;
};
