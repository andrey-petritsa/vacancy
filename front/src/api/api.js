import {urls} from "./urls.js";

export async function show_vacancies_cards(search_query) {
  const url = `${urls.backend}/show_vacancies_cards?${new URLSearchParams(search_query)}`
  const headers = {"Content-Type": "application/json", "X-TOKEN": localStorage.getItem("user_token")}
  const response = await fetch(url, {headers: headers})
  const data = await response.json()
  return data.vacancies_cards
}

export async function change_vacancy_status(id, status) {
  const headers = {"Content-Type": "application/json", "X-TOKEN": localStorage.getItem("user_token")}
  const url = `${urls.backend}/change_vacancy_status`
  await fetch(url, {
    method: "POST",
    headers: headers,
    body: JSON.stringify({
      vacancy_id: id,
      vacancy_status: status
    })
  });
}


export async function show_short_vacancies_cards(search_query) {
  const url = `${urls.backend}/show_short_vacancies_cards?${new URLSearchParams(search_query)}`
  const headers = {"Content-Type": "application/json", "X-TOKEN": localStorage.getItem("user_token")}
  const response = await fetch(url, {headers: headers})
  const data = await response.json()
  return data.short_vacancies_cards
}

export async function generate_cover_latter(vacancy_text) {
  const url = `${urls.backend}/generate_cover_latter`
  const headers = {"Content-Type": "application/json", "X-TOKEN": localStorage.getItem("user_token")}
  const response = await fetch(url, {
    method: "POST",
    headers: headers,
    body: JSON.stringify({ text: vacancy_text })
  })
  const data = await response.json()
  return data.cover_latter
}

export async function show_user(token) {
  const url = `${urls.backend}/show_user/${encodeURIComponent(token)}`
  const res = await fetch(url)
  if (!res.ok) {
    let message = 'Ошибка авторизации'
    try {
      const data = await res.json()
      message = data?.message || message
    } catch (_) {
    }
    throw new Error(message)
  }
  const data = await res.json()
  return data.user
}