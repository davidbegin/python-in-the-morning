import System.Process

-- do is syntax sugar for bind?
-- (>>=)

data Optional a = None | Some a

main = 
  readProcess "beginbot" ["hello"] "" >>= putStrLn

main' :: IO ()
main = do
  -- <- unwrapping
  result <- readProcess "beginbot" ["hello"] ""
  putStrLn 
