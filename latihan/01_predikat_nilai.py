class predikat:
	"""Menentukan predikat berdasarkan nilai akhir."""

	@staticmethod
	def tentukan(nilai):
		if nilai >= 85:
			return "A"
		if nilai >= 70:
			return "B"
		if nilai >= 60:
			return "C"
		if nilai >= 50:
			return "D"
		return "E"


nilai = float(input("Nilai akhir (0-100): "))
hasil_predikat = predikat.tentukan(nilai)
print(f"Nilai {nilai:.2f} memperoleh predikat {hasil_predikat}.")
