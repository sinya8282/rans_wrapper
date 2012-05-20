#include <rans.hpp>
#include "rans.h"

#define SELF static_cast<RANS*>(self)

compile::compile(const std::string& regex)
{
  self = static_cast<void*>(new RANS(regex));
}

compile::~compile()
{
  delete SELF;
}

std::string compile::val(const std::string& text)
{
  return SELF->val(text).get_str();
}

std::string compile::rep(const std::string& value)
{
  return SELF->rep(RANS::Value(value));
}

std::string compile::compress(const std::string& text)
{
  return SELF->compress(text);
}

std::string compile::decompress(const std::string& text)
{
  return SELF->decompress(text);
}

bool compile::accept(const std::string& text)
{
  return SELF->accept(text);
}

unsigned int compile::size()
{
  return SELF->size();
}

#undef SELF
